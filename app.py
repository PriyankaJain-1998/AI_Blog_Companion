import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# from apikey import google_gemini_api_key, openai_api_key

# from openai import OpenAI
# from streamlit_carousel import carousel

# single_img = dict(title = "", 
#      text="",
#      interval=None,
#      img="")
# client = OpenAI(api_key=openai_api_key)
google_gemini_api_key = os.environ.get('google_gemini_api_key')
openai_api_key = os.environ.get('openai_api_key')

genai.configure(api_key=google_gemini_api_key)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

## Setting up our model 
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

## set app to wide
st.set_page_config(layout="wide")

## Title of an app
st.title("Your own AI blog companion")

## Create a subheader
st.subheader("Now you can craft perfect blogs using AI")

## Sidebar for user input
with st.sidebar:
    st.title("Input your blog details")
    st.subheader("Enter details of the blog you wish to generate")

    ## Blog title from the user input
    blog_title = st.text_input("Blog Title")

    ## keywords input
    keywords = st.text_area("Mention the relevant keywords (comma-separated)")

    ## Number of words user wants the blog of
    num_words = st.slider("Number of Words", min_value=250, max_value=1000, step=50)

    ## number of images user wish to generate in this blog 
    # num_images = st.number_input("Number of Images", min_value=0, max_value=10, step=1)

    ## Gemini promt part 
    convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": [f"generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."]
    },
    # {
    #     "role": "model",
    #     "parts": ["**Effect of Generative AI: A Paradigm Shift in Technology and Society**\n\n**Introduction**\nThe advent of generative artificial intelligence (AI) has ushered in an era of unprecedented technological innovation. With its ability to generate novel and creative content, generative AI is poised to revolutionize industries, shift societal paradigms, and pose profound ethical challenges.\n\n**Artificial Creativity and Machine Learning Applications**\nGenerative AI empowers machines to create highly realistic and original content, ranging from text and music to images and videos. This transformative capability stems from advanced machine learning algorithms that learn from vast datasets to identify patterns and synthesize new ideas. By leveraging this artificial creativity, generative AI is facilitating breakthroughs in fields such as entertainment, design, and scientific research.\n\n**Ethical Implications**\nWhile generative AI offers immense potential, it also raises a host of ethical concerns. One primary issue is the potential for misuse and deception. The ability to create realistic content can be exploited for malicious purposes, such as spreading misinformation or creating fake news. Furthermore, the nature of AI-generated content challenges traditional notions of authorship and intellectual property rights.\n\n**Technology Innovation and Economic Impact**\nThe adoption of generative AI is expected to drive significant technology innovation. It will empower businesses with new tools to streamline processes, improve customer experiences, and develop groundbreaking products. The economic impact is likely to be profound, with the potential to create new industries and disrupt existing ones.\n\n**AI Impact on Society**\nGenerative AI has the power to shape society in both positive and negative ways. On the positive side, it can enhance accessibility to education, provide personalized experiences, and contribute to scientific advancements. However, it also poses the risk of job displacement, exacerbation of inequality, and the potential for social unrest due to its impact on traditional employment models.\n\n**Balancing Progress and Responsibility**\nTo harness the transformative power of generative AI while mitigating its potential risks, it is crucial to strike a balance between progress and responsibility. This requires a proactive approach to ethics, regulation, and education. Governments, researchers, and industry leaders must work together to establish guidelines, promote transparency, and foster public understanding.\n\n**Conclusion**\nGenerative AI is a disruptive force that promises to reshape our world in profound ways. While its potential for technological innovation and societal progress is undeniable, it also presents ethical challenges that must be addressed thoughtfully. By embracing a responsible and collaborative approach, we can navigate the complexities of generative AI and unlock its full potential while safeguarding our values and ensuring the benefit of all."]
    # },
    ])

    history = convo.history
    for item in history:
        # Extract the 'parts' content
        parts_content = item.parts[0]



    ## Submit button
    submit_button = st.button("Generate Blog")

if submit_button:
    # response = convo.send_message(blog_title)
    response = model.generate_content(parts_content)


    ### ----- Code to generate relevant images 
    
    # images_gallery = []
    # images = []
    # for i in range(num_images):
    #     img_response = client.images.generate(
    #     model="dall-e-3",
    #     prompt= f"Generate a blog post image on the title : {blog_title}",
    #     size="1024x1024",
    #     quality="standard",
    #     n=1,
    #     )

    #     new_img = single_img.copy()
    #     new_img["title"]=f"Image {i+1}"
    #     new_img["text"] = f"{blog_title}"
    #     new_img['img'] = img_response.data[0].url

    #     images_gallery.append(new_img)
        # images.append(img_response.data[0].url)
        # image_url = img_response.data[0].url

    # for i in range(num_images):
    #     st.write(images[i])
        
    # carousel(items=images_gallery, width=1)
    
    # st.image(image_url, caption="Generated Image")
    st.title("YOUR BLOG POST :")
    st.write(response.text)