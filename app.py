from dotenv import load_dotenv
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceHub
from langchain.memory import SimpleMemory
# import pyper Clip for Copy Response Text
import pyperclip as clip
def css():
   return '''
<style>
.text_{
    width:100%;
    border: 1px solid rgba(49, 51, 63, 0.2);
    padding:10px;
    border-radius:0.5rem;
}
</style>
'''

def text(title,category,Tone,Words,keywords,style,section):
    llm=HuggingFaceHub(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",model_kwargs={
        "max_new_tokens": 912,
        "top_k": 30,
        "temperature": 0.1,
        "repetition_penalty": 1.03,
    })
    Template='''write a Blog about this title "{title}".Which have round about {Words} related to the specific Niche or type {category} with having {section} section . Each section have related heading, sub heading and bullet points to break up the text and make it more visually appealing about giving title of Blog. A tone and style of Blog is giving more efficient , appropriate reliably for understanding human to engage it Thats why the tone of Blog is {Tone} and style of Blog is {style}.
Now there are some {Keywords} keywords related for this Blog which you will target it with naturally and best strategy to optimize. which not have been showing keyword stuffing.
Follow these guidelines writing this content:
* The blog post should be written in *easy English* that is *easy to read* and *should be written in human tone and style which have I define you* and *not look like AI generated*
* The Blog meets Google's requirements and their Terms and Condition for helpful content updates.
* Use natural language and avoid using jargon or technical terms that the average reader may not understand.
* Use active voice instead of passive voice.
* Use contractions and other informal language where appropriate.
* Use humour and other elements of human emotion to engage the reader.
* Avoid using clichés or overused phrases.
* Proofread the text carefully before submitting it.

Last, giving 2 Prompt for Generating Related Image for This Blog.
'''
    Prompt=PromptTemplate(template=Template,input_variables=['title','category','section','Tone','Words','Keywords','style'])
    chain=LLMChain(llm=llm,prompt=Prompt)
    output=chain.run({'title':title,'category':category,'section':section,'Tone':Tone,'Words':Words,'Keywords':keywords,'style':style})
    return output

def structure():
    load_dotenv()
    st.set_page_config(page_icon=":book:",page_title='Article Generator App')
    st.header("*Article* Generator :blue[App]")
    st.write(css(),unsafe_allow_html=True)
   
    global html
    html=''
    blog_type=(
'Personal ',
'Lifestyle ',
'Travel ',
'Food ',
'Fashion ',
'Parenting ',
'Fitness/Health ',
'Tech ',
'Business/Entrepreneurship ',
'News and Current Affairs ',
'Educational ',
'Book (Book Review)',
'Photography ',
'Political ',
'Environmental/Sustainability ',
'DIY/Craft ',
'Gaming ',
'Review ',
'Finance ',
'Educational Technology(EdTech) ',
)
    tones=(
"Casual/Conversational",
"Professional",
"Humorous/Light hearted",	
"Inspirational/Motivational",
"Educational/Informative",
"Opinionated",
"Sarcastic/Satirical",
"Empathetic/Supportive",
"Adventurous/Exploratory",
"Controversial/Provocative",
"Nostalgic/Reflective",
"Friendly/Approachable",
"Objective/Neutral",
"Interactive/Engaging"
)

    styles=(
'Conversational',
'Educational/Informative',
'Storytelling',
'Listicle',
'How-to/Guide',
'Opinion/Personal Reflection',
'Interviews',
'Review/Recommendation',
'Humorous/Satirical',
'Motivational/Inspirational',
'Guest Posts',
'News/Updates',
'Q&A/FAQs',
'Behind-the-Scenes',
'Photo/Visual-Centric',
'Interactive',
'Seasonal/Themed',
'Trend Analysis'
)

    with st.form("my_form"):
        st.write("Enter Your Related <b>Article</b>",unsafe_allow_html=True)
        title=st.text_input(label='Article Title')
        col1,col2=st.columns(2)
        with col1:
           category=st.selectbox('Related Category',options=blog_type,index=None,placeholder='Select Any Category')
           Tone=st.selectbox('Tones Related For Article',options=tones,placeholder='Select Any Tone',index=None)
           style=st.selectbox('Style Related For Article',options=styles,placeholder='Select Any Style',index=None)
        with col2:
           Words=st.number_input('No. Of Words')
           keywords=st.text_input('Keywords for SEO',placeholder='Enter kwds with comma seperate')
           section=st.number_input('No. of Section')
        submitted = st.form_submit_button("Submit")
        if submitted:
         if title == '' or category == '' or  Tone =='' or  Words== '' or keywords == "" or section == '' or style == '':
            st.warning('Please Enter All Field..')        
         else:
            # st.write([title,category,Words,keywords,Tone,style,section])
           html=text(title=title,category=category,Tone=Tone,Words=Words,keywords=keywords,style=style,section=section)
        #    st.session_state.response=html   
    with st.container(border=True):
        if html:
           st.write(html)
           
if __name__ == '__main__':
    structure()