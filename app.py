import streamlit as st

st.title("GeneScope")
st.subheader("Smart DNA Sequence Analysis System")

dna = st.text_input("Enter DNA Sequence")

if st.button("Analyze"):

    dna = dna.upper()

    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")

    length = len(dna)

    if length == 0:
        st.error("Please enter DNA sequence")
    else:

        gc = ((g+c)/length)*100

        st.write("Length:", length)
        st.write("A Count:", a)
        st.write("T Count:", t)
        st.write("G Count:", g)
        st.write("C Count:", c)
        st.write("GC Content:", round(gc,2), "%")

        reverse = dna[::-1]

        st.write("Reverse Sequence:", reverse)
