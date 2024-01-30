# Aplikasi Klasifikasi Awan menggunakan MobileNetV2

![Awan](https://images.theconversation.com/files/358278/original/file-20200916-20-vuw2hi.jpg?ixlib=rb-1.1.0&rect=21%2C7%2C4723%2C3151&q=20&auto=format&w=320&fit=clip&dpr=2&usm=12&cs=strip)

## Deskripsi

Aplikasi ini menggunakan model MobileNetV2 untuk melakukan klasifikasi awan berdasarkan jenisnya. Dengan antarmuka pengguna yang ramah, aplikasi ini memungkinkan pengguna untuk mengunggah gambar awan dan mendapatkan hasil klasifikasi secara real-time.

## Cara Menjalankan Aplikasi

1. Pastikan Anda memiliki Python terinstal. Jika belum, Anda dapat mengunduhnya dari [Python Official Website](https://www.python.org/).

2. Clone repositori ini ke dalam direktori lokal:

    ```bash
    git clone https://github.com/arfianaja/deteksi_jenis_awan.git
    ```

3. Pindah ke direktori aplikasi:

    ```bash
    cd deteksi_jenis_awan
    ```

4. Install dependensi:

    ```bash
    pip install -r requirements.txt
    ```

5. Jalankan aplikasi:

    ```bash
    streamlit run main.py
    ```

6. Buka browser dan buka alamat [http://localhost:8501](http://localhost:8501) untuk melihat aplikasi.

## Penggunaan Aplikasi

1. Unggah gambar awan yang ingin diklasifikasikan.
2. Aplikasi akan melakukan klasifikasi dan menampilkan hasilnya.
3. Nikmati hasil klasifikasi dan informasi tambahan yang ditampilkan.
4. jika akurasi di bawah 70% maka hasil pendeteksian akan di anggap gagal mendeteksi

## Kontribusi

Jika Anda ingin berkontribusi pada pengembangan aplikasi ini, kami menyambut kontribusi melalui _pull request_. Silakan ikuti pedoman kontribusi kami dalam file `CONTRIBUTING.md`.

## Lisensi

Diprogram dengan ❤️ oleh Arpian.

