import streamlit as st
from utility.login import Login
from utility.get_data import get_intents
import os


class Run(Login):
    DATA_PATH = "./custom_data/"

    def __init__(self):
        super().__init__()

    def access_approved(self):
        placeholder = st.empty()

        while True:
            if 'num' not in st.session_state:
                st.session_state.num = 1
            if 'topic' not in st.session_state:
                st.session_state.topic = sorted(list(get_intents().keys()))[0]

            with placeholder.container():
                num = st.session_state.num

                # Get all intents
                topics = sorted(list(get_intents().keys()))
                topic = st.selectbox(label="Topic", options=topics, key=num,
                                     index=topics.index(st.session_state.topic))

                # Show data in file intent and utter
                col1, col2 = st.columns(2)
                with col1:
                    intent_filename = "intent_" + topic + ".yml"

                    with open(self.DATA_PATH + "intent/" + intent_filename, "r") as file:
                        raw_data = file.read()
                        intent_data = st.text_area(label=intent_filename, value=raw_data, height=300)

                    with open(self.DATA_PATH + "intent/" + intent_filename, "w") as file:
                        save = st.button("Save intent", key=num)
                        if save:
                            file.write(intent_data)
                        else:
                            file.write(raw_data)
                with col2:
                    utter_filename = "utter_" + topic + ".yml"

                    with open(self.DATA_PATH + "utter/" + utter_filename, "r") as file:
                        raw_data = file.read()
                        utter_data = st.text_area(label=utter_filename, value=raw_data, height=300)

                    with open(self.DATA_PATH + "utter/" + utter_filename, "w") as file:
                        save = st.button("Save utter", key=num)
                        if save:
                            file.write(utter_data)
                        else:
                            file.write(raw_data)

                # More features
                advance = st.checkbox("Advance", key=num)

                if advance:
                    feature = st.radio("Choose advance feature:", ("Create topic", "Delete topic"), key=num)

                    if feature == "Create topic":
                        new_topic = st.text_input("New topic")

                        create = st.button("Create", key=num)
                        if create:
                            intent_path = self.DATA_PATH + "intent/" + "intent_" + new_topic + ".yml"
                            utter_path = self.DATA_PATH + "utter/" + "utter_" + new_topic + ".yml"

                            try:
                                with open(intent_path, 'x') as f:
                                    f.write("- intent: {intent_name}\n  examples: |\n    - {Write some sentences}")
                                with open(utter_path, 'x') as f:
                                    f.write("  {utter_name}:\n  - text: \"{Write some sentences}\"")
                            except FileExistsError:
                                st.write("This name has already exists. Please insert a different name.")

                            st.session_state.num += 1
                            st.session_state.topic = new_topic
                            placeholder.empty()
                        else:
                            st.stop()

                    if feature == "Delete topic":
                        st.markdown("<div style='font-size: 25px; color:red'>Delete current topic?</div>",
                                    unsafe_allow_html=True)

                        delete = st.button("Delete", key=num)
                        if delete:
                            intent_path = self.DATA_PATH + "intent/" + "intent_" + topic + ".yml"
                            utter_path = self.DATA_PATH + "utter/" + "utter_" + topic + ".yml"

                            os.remove(intent_path)
                            os.remove(utter_path)
                            delattr(st.session_state, "topic")

                            st.session_state.num += 1
                        else:
                            st.stop()
                else:
                    st.stop()


if __name__ == "__main__":
    run = Run()
