# Perbandingan-Kinerja-Web-Server-Pemrograman-Jaringan-

--SOAL--

- Dengan memanfaatkan program pada progjar5
 
 https://github.com/rm77/progjar/tree/master/progjar5
 
- Gunakan contoh source code yang disediakan, untuk dimodifikasi

- Gunakan instalasi lab anda sendiri

- Implementasikan web server dengan multiprocessing

- Buatlah perbandingan kinerja web server

 https://github.com/rm77/progjar/blob/master/progjar5/server_thread_http.py
 dengan:
 
1. Multithreading
2. Multiprocessing
3. Multithreading (secure)
4. Multiprocessing (secure)

- Untuk pengukuran kinerja, gunakan toolab (apache-benchmark) dengan jumlah request 1000, dengan parameter concurrency 10,50,100,150,200

- Laporkan kinerja dalam hal:

Failed requests, Total Transfer, request per second, Time per
 request, Transfer Rate , connect, processing, waiting, total
 connection time--

 
 *** untuk meningkatkan performa, hilangkan beberapa overhead
 seperti print/mencetak log seluruh isi direktori/folder
 Apache-benchmark dapat diinstall di ubuntu/debian dengan
sudo apt install apache2-utils
