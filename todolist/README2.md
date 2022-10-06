# Assignment 5 PBP

Nama  : Erlangga Ahmad Khadafi

NPM   : 2106750894

Kelas : PBP-B

## LINK

Main Page           : https://tugas2dafi.herokuapp.com/

Katalog Page        : https://tugas2dafi.herokuapp.com/katalog/

MyWatchlist Page    : https://tugas2dafi.herokuapp.com/mywatchlist/

ToDoList Page       : https://tugas2dafi.herokuapp.com/todolist/

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

<h2>1. Inline CSS</h2>

Dalam Inline CSS, kita meletakkan property CSS pada attribute tag HTML, sebagai contoh:
```
<h1 style="color:blue;text-align:center;">Hello</h1>
```
<h3>Kelebihan: </h3>

- Dapat mengkostumisasi tiap element tanpa memikirkan dampaknya pada elemen lain

<h3>Kekurangan: </h3>

- Attribute dari tiap elemen akan menjadi sangat panjang
- Mungkin terjadi banyak pengulangan

<br>

<h2>2. Internal CSS</h2>

Dalam Internal CSS, attribute CSS ditulis di dalam tag `<style>` pada file HTML.

<h3>Kelebihan</h3>

- Tidak perlu membuat file HTML dan seluruh attribute CSS menjadi satu kesatuan

<h3>Kekurangan</h3>

- Dokumen dapat menjadi kurang bersih karena attribute CSS bercampur dengan dokumen HTML

<br>

<h2>3. External CSS</h2>

Dalam external CSS, attribute CSS ditulis di luar file HTML. Hal ini bisa dilakukan dengan membuat file .css baru, lalu import ke file HTML, sebagai berikut:
```
<link rel="stylesheet" href="example.css"/>
```

<h3>Kelebihan</h3>

- Dapat membuat banyak properti

<h3>Kekurangan</h3>

- Cenderung kompleks dan kurang efektif untuk dokumen singkat

<br>
<hr>

## Jelaskan tag HTML5 yang kamu ketahui.

<br>

1. `<head>` berisi informasi terkait dokumen
2. `<body>` menyatakan isi dari dokumen
3. `<h1>` hingga `<h6>` melambangkan headings mulai dari yang terbesar hingga terkecil
4. `<img>` merepresentasikan gambar atau foto
5. `<button>` untuk tombol
6. `<br>` untuk line break atau baris kosong
7. `<hr>` untuk garis horizontal
8. `<p>` untuk paragraf
9. `<form>` untuk form
10. `<input>` untuk menerima input dari user
11. `<div>` yang melambangkan bagian tertentu dari dokumen

<br>
<hr>

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

<br>

1. Element selector
-> Menggunakan tag HTML untuk menerapkan styling.
2. Class selector
-> Menggunakan class untuk menerapkan styling dengan format `.[nama_kelas]`.
3. ID selector
-> Menggunakan id untuk menerapkan styling dengan format `#[id]`.


<br>
<hr>

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

<br>

1. Pada folder templates pada file base html di dalam tag `<style>` tambahkan CSS untuk styling dan tidak lupa untuk meng-import bootstrap.
2. Tambahkan styling untuk create_task.html, login.html, register.html, dan todolist.html.
3. Pada todolist.html buat cards untuk tiap task-nya.
4. Push lalu deploy ke Heroku.