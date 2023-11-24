import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

# Set the page width
st.set_page_config(layout="wide")

# Load the trained MobileNetV2 model
model = tf.keras.models.load_model('model.h5')

# Set the labels for classification
class_names = ['cumulus', 'cumulunimbus', 'stratus', 'nimbostratus', 'stratocumulus']

# Set the page title and description
st.title('Klasifikasi Jenis Awan')
st.write('Upload gambar')

# Create a file uploader
uploaded_file = st.file_uploader('Pilih gambar...', type=['jpg', 'jpeg', 'png'])

button_col1, button_col2 = st.columns([1,19])
detect_button = button_col1.button('Deteksi')

#  Display the reset button only when the image is uploaded
if uploaded_file and detect_button:
    reset_button = button_col2.button('Reset')

if detect_button:
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
        image = tf.keras.applications.mobilenet_v2.preprocess_input(image)

        # Perform the classification
        predictions = model.predict(image)

        # Get the predicted class index
        predicted_class_index = np.argmax(predictions)
        predicted_class = class_names[predicted_class_index]

        # Get top 2 class indices and probabilities
        top_2_indices = np.argsort(predictions[0])[::-1][:2]
        top_2_probabilities = predictions[0][top_2_indices]
        top_2_class_names = [class_names[i] for i in top_2_indices]

        if 'reset_button' in st.session_state and st.session_state.reset_button:
            uploaded_file = None
            st.session_state.reset_button = False


        # Display the uploaded image and classification results
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
            # Menyembunyikan informasi jika tombol reset telah diklik
            if uploaded_file and top_2_probabilities[0] >= 0.7:
                if predicted_class == 'cumulus':
                    st.write('Informasi tentang Cumulus:')
                    col1, col2 = st.columns([3, 2])
                    with col2:
                        # Specify the path to your image in the assets folder
                        image_path = 'assets/cumulus.jpg'  # Update with your image file name and path

                        # Display the image
                        st.image(image_path, caption='Cumulus Image', width=500)

                    with col1:
                        st.subheader('Definisi')
                        st.write('Awan terpisah, umumnya padat dan bergaris tajam, berkembang secara vertical bentuk gundukan, kubah atau menara, bagian atasnya menonjol menyerupai kembang kol. Bagian atas awan yang diterangi matahari sebagina besar berwarna putih cemerlang, alasnya relatif gelap dan hampir horizontal. Terkadang cumulus compang-camping.')
                        st.subheader('Konstitusi Fisik')
                        st.write('Cumulus sebagian besar terdiri dari tetesan air. Ketika berapa pada ketinggian vertical yang besar, cumulus dapat melepaskan presipitasi dalam bentuk hujan.')
                        st.subheader('Penafsiran')
                        st.write('Awan cuaca bagus. Jika awan ini mencapai tingkat atmosfer sedang dan berubah menjadi awan cumulonimbus hujan ringan mungkin saja terjadi.')

                elif predicted_class == 'cumulunimbus':
                        st.write('Informasi tentang Cumulunimbus:')
                        col1, col2 = st.columns([3,2])
                        with col2:
                            # Specify the path to your image in the assets folder
                            image_path = 'assets/cumulunimbus.jpg'  # Update with your image file name and path
                                
                            # Display the image
                            st.image(image_path, caption='Cumulunimbus Image', width=500)
                            
                        with col1:
                            st.subheader('Definisi')
                            st.write('Awan tebal dan padat, dengan bentangan vertikal cukup luas, berbentuk gunung atau menara besar. Setidaknya sebagian dari bagian atasnya biasanya halus, berserat atau lurik, dan hampir selalu rata; bagian ini sering menyebar dalam bentuk landasan atau bulu-bulu yang luas.  Di bawah dasar awan ini, yang seringkali sangat gelap, sering kali terdapat awan-awan rendah yang tidak rata, baik menyatu atau tidak, dan curah hujan terkadang dalam bentuk virga.')
                            st.subheader('Konstitusi Fisik')
                            st.write('Cumulonimbus terdiri dari tetesan air dan, terutama di bagian atasnya, kristal es. Ini juga berisi tetesan hujan besar dan, sering kali, butiran salju, butiran salju, atau batu es. Tetesan air dan tetesan hujan mungkin menjadi sangat dingin.')
                            st.subheader('Penafsiran')
                            st.write('Curah hujan lebat, seringkali disertai badai petir.')


                    # Tambahkan bagian lainnya untuk kelas lain

                elif predicted_class == 'stratus':
                        st.write('Informasi tentang Stratus:')
                        col1, col2 = st.columns([3,2])
                        with col2:
                            # Specify the path to your image in the assets folder
                            image_path = 'assets/stratus.jpg'  # Update with your image file name and path
                            
                            # Display the image
                            st.image(image_path, caption='Stratus Image', width=500)
                        
                        with col1:
                            st.subheader('Definisi')
                            st.write('Umumnya lapisan awan yang berwarna abu-abu dengan dasar cukup seragam yang dapat menghasilkan gerimis. Ketika matahari terlihat melalui awan, garis luarnya terlihat jelas. Terkadang stratus muncul dalam bentuk tambalan yang tidak rata.')
                            st.subheader('Konstitusi Fisik')
                            st.write('Stratus biasanya terdiri dari tetesan air kecil. Stratus dapat menghasilkan mahkota di sekitar matahari atau bulan. Awan lapisan rendah digambarkan sebagai kabut tinggi atau kabut diatas permukaan tanag. Pada suhu rendah stratus mungkin terdiri dari partikel es kecil. Stratus bila padat atau tebal, seringkali berisi tetesan gerimis. Tampilannya yang gelap atau bahkan mengancam.')
                            st.subheader('Penafsiran')
                            st.write('Umumnya menunjukan kondisi cuaca yang agak tenang')
                    
                elif predicted_class == 'nimbostratus':
                        st.write('Informasi tentang Nimbrostratus:')
                        col1, col2 = st.columns([3,2])
                        with col2:
                            # Specify the path to your image in the assets folder
                            image_path = 'assets/nimbostratus.jpg'  # Update with your image file name and path
                            
                            # Display the image
                            st.image(image_path, caption='Nimbostratus Image', width=500)
                        
                        with col1:
                            st.subheader('Definisi')
                            st.write('Lapisan awan kelabu, seringkali gelap, penampakannya menyebar karena hujan yang terus-menerus. Lapisan yang cukup tebal untuk menutupi sinar matahari. Awan rendah dan tidak rata sering kali muncul di bawah lapisan, yang mungkin menyatu atau tidak.')
                            st.subheader('Konstitusi Fisik')
                            st.write('Stratocumulus terdiri dari tetesan air, terkadang disertai tetesan hujan atau yang lebih jarang, butiran salju, kristal salju dan kepingan salju. Kristal es apa pun yang ada biasanya terlalu panjang untuk membuat awan tampak berserat. Ketika stratocumulus tidak terlalu tebal, kadang-kadang terlihat korona atau irisasi.')
                            st.subheader('Penafsiran')
                            st.write('Hujan, hujan jangka panjang selama beberapa jam/hari')
                    
                elif predicted_class == 'stratocumulus':
                        st.write('Informasi tentang Stratocumulus:')
                        col1, col2 = st.columns([3,2])
                        with col2:
                            # Specify the path to your image in the assets folder
                            image_path = 'assets/stratocumulus.jpg'  # Update with your image file name and path
                            
                            # Display the image
                            st.image(image_path, caption='Stratocumulus Image', width=500)
                        
                        with col1:
                            st.subheader('Definisi')
                            st.write('Abu-abu, keputihan atau keduanya, bercak, lembaran atau lapisan awan yang hampir selalu memiliki bagian gelap, massa bulat, gulungan, dan lain lain, yang tidak berserat dan yang mungkin atau tidak boleh digabungkan, sebagian besar unsur-unsur kecil yang tersusun beraturan mempunyai lebar lebih dari 5.')
                            st.subheader('Konstitusi Fisik')
                            st.write('Nimbostratus umumnya mencakup wilayah yang luas dan luasnya secara vertical. Ini terdiri dari tetesan air (terkadang sangat dingin) atau campuran partikel cair dan padat. Konsentrasi partikel yang tinggi dan luasnya awan secara vertikal menghalangi sinar matahari langsung untuk dapat diamati melaluinya. awan nimbostratus dapat ditemukan relatif dekat dengan permukaan tanah, namun puncaknya dapat memanjang hingga ketingkat awan tengah. Ketebalan awan nimbostratus membantu memberikan tampilan yang lebih gelap dibandungkan awan lainnya.')
                            st.subheader('Penafsiran')
                            st.write('Terkadang hujan, umumnya menandakan ketidakstabilan atmosfer. Terjadi tepat sebelum oklusi antara front dingin dan front hangat.')
                else:
                    st.write('Informasi tentang kelas lainnya')
