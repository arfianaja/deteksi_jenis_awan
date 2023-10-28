import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Set the page width
st.set_page_config(layout="wide")

# Load the trained model
model = tf.keras.models.load_model('keras_model.h5')

# Set the labels for classification
class_names = ['cumulus', 'cumulunimbus', 'stratus', 'nimbostratus',  'stratocumulus']

# Set the page title and description
st.title('Klasifikasi Jenis Awan')
st.write('Upload gambar')

# Create a file uploader
uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

if st.button('Deteksi'):
    if uploaded_file is not None:
        # Read the image file
        image = Image.open(uploaded_file)

        # Resize the image to the required input shape of the model
        image = image.resize((224, 224))

        # Convert the image to a NumPy array
        image = tf.keras.preprocessing.image.img_to_array(image)

        # Expand the dimensions of the image to match the input shape of the model
        image = tf.expand_dims(image, axis=0)

        # Preprocess the image
        image = tf.keras.applications.resnet50.preprocess_input(image)

        # Perform the classification
        predictions = model.predict(image)
        predictions = np.squeeze(predictions)  # Menghapus dimensi yang tidak perlu

        predicted_class_index = np.argmax(predictions)
        predicted_class = class_names[predicted_class_index]

        # Get top 3 class probabilities and corresponding class names
        top_2_indices = np.argsort(predictions)[::-1][:2]
        top_2_probabilities = predictions[top_2_indices]
        top_2_class_names = [class_names[i] for i in top_2_indices]

        # Menampilkan gambar, kelas yang diprediksi, dan akurasi per kelas
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(uploaded_file, caption='Gambar yang Diunggah', width=400)

        with col2:
            st.write('Kelas yang Diprediksi:', predicted_class)
            st.write('Probabilitas Teratas 2 Kelas:')
            for i in range(len(top_2_class_names)):
                if top_2_class_names[i] == predicted_class:
                    bar_color = 'orange'
                    label_color = 'orange'
                else:
                    bar_color = 'blue'
                    label_color = 'black'
                st.write(f'{top_2_class_names[i]}: {top_2_probabilities[i]*100:.2f}%')
                placeholder = st.empty()
                placeholder.markdown(
                    f'<div style="background-color: {bar_color}; width: {top_2_probabilities[i]*100}%; height: 25px;"></div>',
                    unsafe_allow_html=True
                )

        # Expander untuk informasi tentang kelas awan
        expander = st.expander('Informasi Lengkap')
        with expander:
            if predicted_class == 'Altocumulus':
                col1, col2 = st.columns([1,3])
                with col2:
                    st.write('Informasi tentang Altocumulus:')

                with col1:
                    st.write('jjsdjhds')

            elif predicted_class == 'Altostratus':
                st.write('Informasi tentang Altostratus:')
                col1, col2 = st.columns([1, 3])
                
                with col1:
                    st.subheader('Bentuk')
                    st.write('Bentuk')
                    st.subheader('Keterangan')
                    st.subheader('Berpotensi')

             # Tambahkan bagian lainnya untuk kelas lain

            elif predicted_class == 'stratus':
                st.write('Informasi tentang Stratus:')
                col1, col2 = st.columns([1,3])
                with col2:
                    url = 'https://id.wikipedia.org/wiki/Stratus'  # Ganti dengan URL website yang tepat
                    html_code = f'<iframe src="{url}" width="1000" height="600"></iframe>'
                    st.components.v1.html(html_code, height=800)
                
                with col1:
                    st.subheader('Bentuk')
                    st.write('Bentuk')
                    st.subheader('Keterangan')
                    st.subheader('Berpotensi')

            elif predicted_class == 'cumulunimbus':
                st.write('Informasi tentang Cumulonimbus:')
                col1, col2 = st.columns([1,3])
                with col2:
                    url = 'https://id.wikipedia.org/wiki/Awan_kumulonimbus'  # Ganti dengan URL website yang tepat
                    html_code = f'<iframe src="{url}" width="1000" height="600"></iframe>'
                    st.components.v1.html(html_code, height=800)

                with col1:
                    st.subheader('Bentuk')
                    st.write('Bentuk')
                    st.subheader('Keterangan')
                    st.subheader('Berpotensi')

            elif predicted_class == 'Cirromulus':
                st.write('Informasi tentang Cirromulus:')
                col1, col2 = st.columns([1,3])
                with col2:
                    url = 'https://id.wikipedia.org/wiki/Awan_sirokumulus'  # Ganti dengan URL website yang tepat
                    html_code = f'<iframe src="{url}" width="1000" height="600"></iframe>'
                    st.components.v1.html(html_code, height=800)

                with col1:
                    st.subheader('Bentuk')
                    st.write('Bentuk')
                    st.subheader('Keterangan')
                    st.subheader('Berpotensi')
            
            elif predicted_class == 'Cirrus':
                st.write('Informasi tentang Cirrus:')
                col1, col2 = st.columns([1,3])
                with col2:
                    url = 'https://id.wikipedia.org/wiki/Awan_sirus'  # Ganti dengan URL website yang tepat
                    html_code = f'<iframe src="{url}" width="1000" height="600"></iframe>'
                    st.components.v1.html(html_code, height=800)
                
                with col1:
                    st.subheader('Bentuk')
                    st.write('Bentuk')
                    st.subheader('Keterangan')
                    st.subheader('Berpotensi')
            
            elif predicted_class == 'Cirrostratus':
                st.write('Informasi tentang Cirrostratus:')
                col1, col2 = st.columns([1,3])
                with col2:
                    url = 'https://id.wikipedia.org/wiki/Awan_sirostratus'  # Ganti dengan URL website yang tepat
                    html_code = f'<iframe src="{url}" width="1000" height="600"></iframe>'
                    st.components.v1.html(html_code, height=800)

                with col1:
                    st.subheader('Bentuk')
                    st.write('Bentuk')
                    st.subheader('Keterangan')
                    st.subheader('Berpotensi')
            
            elif predicted_class == 'cumulus':
                st.write('Informasi tentang Cumulus:')
                col1, col2 = st.columns([1,3])
                with col2:
                    url = 'https://id.wikipedia.org/wiki/Awan_kumulus'  # Ganti dengan URL website yang tepat
                    html_code = f'<iframe src="{url}" width="1000" height="600"></iframe>'
                    st.components.v1.html(html_code, height=800)

                with col1:
                    st.subheader('Bentuk')
                    st.write('Bentuk')
                    st.subheader('Keterangan')
                    st.subheader('Berpotensi')
            
            elif predicted_class == 'nimbostratus':
                st.write('Informasi tentang Nimbrostratus:')
                col1, col2 = st.columns([1,3])
                with col2:
                    url = 'https://id.wikipedia.org/wiki/Awan_nimbostratus'  # Ganti dengan URL website yang tepat
                    html_code = f'<iframe src="{url}" width="1000" height="600"></iframe>'
                    st.components.v1.html(html_code, height=800)

                with col1:
                    st.subheader('Bentuk')
                    st.write('Bentuk')
                    st.subheader('Keterangan')
                    st.subheader('Berpotensi')
            
            elif predicted_class == 'stratocumulus':
                st.write('Informasi tentang Stratocumulus:')
                col1, col2 = st.columns([1,3])
                with col2:
                    url = 'https://id.wikipedia.org/wiki/Awan_stratokumulus'  # Ganti dengan URL website yang tepat
                    html_code = f'<iframe src="{url}" width="1000" height="600"></iframe>'
                    st.components.v1.html(html_code, height=800)
                
                with col1:
                    st.subheader('Bentuk')
                    st.write('Bentuk')
                    st.subheader('Keterangan')
                    st.subheader('Berpotensi')
