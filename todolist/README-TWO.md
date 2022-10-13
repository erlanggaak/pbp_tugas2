# Assignment 6 PBP

Nama  : Erlangga Ahmad Khadafi

NPM   : 2106750894

Kelas : PBP-B

## LINK

ToDoList Page       : https://tugas2dafi.herokuapp.com/todolist/

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Pada synchronous programming, task dijalankan satu per satu sehingga pengguna perlu menunggu 
task selesai diproses untuk dapat menjalankan task yang lain. Sementara itu, pada asynchronous programming, 
task dapat dijalankan secara parallel sehingga pengguna tidak perlu menunggu suatu task selesai diproses
untuk dapat menjalankan task yang lain.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming adalah sebuah paradigma di mana suatu task dijalankan sebagai respon/akibat dari terjadinya suatu event.
Contoh penerapan pada tugas ini adalah adanya button yang digunakan sebagai trigger untuk memunculkan modal. Ketika pengguna 
mengeklik button tersebut, maka modal akan muncul.

## Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX adalah AJAX memungkinkan adanya update pada halaman web tanpa perlu melakukan refresh keseluruhan halaman.
Hal tersebut dapat dilakukan karena AJAX memisahkan presentation layer dengan data exchange layer sehingga ketika terjadi perubahan data, 
halaman web tetap dapat ditampilkan dan perubahan data yang dilakukan akan diupdate ketika selesai dijalankan tanpa
harus mengupdate keseluruhan halaman. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

<br>

1. Mengubah method get dan post di `views.py` untuk mengembalikan seluruh data task dalam bentuk JSON
2. Melakukan load data (ambil data dari database dan dikirim sebagai JSON) dan membuat card untuk tiap data tasklist
3. Membuat modal lalu merefer tombol Add Task agar membuka modal tersebut
4. Membuat function Javascript untuk menghandle get, post, dan delete Task dimana tiap function melakukan refresh pada container Task Card.