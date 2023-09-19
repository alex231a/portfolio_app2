import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("John Smith")
    content = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in mi tristique, 
        mattis purus ut, congue nunc. Suspendisse urna nulla, fermentum eget leo sit amet, 
        mollis finibus risus. Vivamus eleifend, nulla vitae rhoncus ultrices, velit quam 
        luctus leo, nec tincidunt orci mi in massa. Vestibulum posuere semper neque sed posuere. 
        Nulla imperdiet convallis tristique. Maecenas ut cursus magna. Sed et tempus velit. 
        Suspendisse urna neque, eleifend et nibh vel, viverra lobortis urna. 
        Nullam id lectus quis enim sollicitudin egestas. Nullam placerat porta enim. 
        Nulla nec arcu molestie, gravida ex nec, tempus ante.
    """
    st.info(content)

content2 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
         "Donec in mi tristique, mattis purus ut, congue nunc. "
         "Suspendisse urna nulla, fermentum eget leo sit amet, mollis finibus risus. "
         "Vivamus eleifend, nulla vitae rhoncus ultrices, velit quam luctus leo, "
         "nec tincidunt orci mi in massa."""
st.write(content2)


col3, empty_cod, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[source code]({row['url']})")