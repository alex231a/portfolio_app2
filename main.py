import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("John Smith")
    content = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in mi tristique, mattis purus ut, congue nunc. Suspendisse urna nulla, fermentum eget leo sit amet, mollis finibus risus. Vivamus eleifend, nulla vitae rhoncus ultrices, velit quam luctus leo, nec tincidunt orci mi in massa. Vestibulum posuere semper neque sed posuere. Nulla imperdiet convallis tristique. Maecenas ut cursus magna. Sed et tempus velit. Suspendisse urna neque, eleifend et nibh vel, viverra lobortis urna. Nullam id lectus quis enim sollicitudin egestas. Nullam placerat porta enim. Nulla nec arcu molestie, gravida ex nec, tempus ante.
    """
    st.info(content)

st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in mi tristique, mattis purus ut, congue nunc. Suspendisse urna nulla, fermentum eget leo sit amet, mollis finibus risus. Vivamus eleifend, nulla vitae rhoncus ultrices, velit quam luctus leo, nec tincidunt orci mi in massa.")
