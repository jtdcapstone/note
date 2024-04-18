import streamlit as st

# In-memory storage for notes
notes = []

# Function to add a note
def add_note(note):
    notes.append(note)

# Function to list notes
def list_notes():
    return notes

# Function to remove a note
def remove_note(note):
    notes.remove(note)

# Streamlit UI
def main():
    st.title("Notepad")

    # Sidebar for adding notes
    with st.sidebar:
        st.header("Add Note")
        note_input = st.text_area("Enter your note:")
        if st.button("Add"):
            if note_input:
                add_note(note_input)
                st.success("Note added successfully!")
            else:
                st.warning("Please enter a note!")

    # Main content to list, edit, and delete notes
    st.header("Your Notes")
    all_notes = list_notes()
    if all_notes:
        for idx, note in enumerate(all_notes, start=1):
            st.write(f"{idx}. {note}")
            # Delete option
            if st.button(f"Delete Note {idx}"):
                remove_note(note)
                st.success("Note deleted successfully!")
    else:
        st.write("No notes added yet.")

if __name__ == "__main__":
    main()
