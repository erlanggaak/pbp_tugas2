# Assignment 2 PBP

Nama  : Erlangga Ahmad Khadafi

NPM   : 2106750894

Kelas : PBP-B

## LINK

Main Page    : https://tugas2dafi.herokuapp.com/

Katalog Page : https://tugas2dafi.herokuapp.com/katalog/

## Bagan Request Django Workflow

![](https://github.com/erlanggaak/pbp_tugas2/blob/main/DjangoArchitectureDiagram.png)

## Virtual Environment

Virtual environment adalah pengisolasian libraries, module, dan script pada suatu project agar libraries tersebut hanya digunakan pada project yang bersangkutan. Tujuan digunakannya virtual environment adalah untuk menjaga project dari perubahan libraries. Sebagai contoh Project A menggunakan libraries X dengan versi 1.0. Kemudian libraries X tersebut terdapat update 1.1 yang mengubah salah satu function. Terdapat kemungkinan logic dan function Project A terpengaruh akibat update tersebut yang mungkin mengakibatkan error ataupun tidak bisa digunakan. Untuk itu kita menggunakan virtual environment untuk setiap project yang akan dibuat.

Mungkin saja apabila kita tidak menggunakan virtual environment untuk mengembangkan website app di Django, namun risiko yang sudah disebutkan diatas dapat saja terjadi dan mengganggu fungsionalitas program

## Implementasi

1. Hal pertama yang dilakukan adalah membuat function show_katalog() yang menerima parameter request untuk dipassing ke function render() bawaan Django. Pada function show_katalog(), simpan semua objects of CatalogItem di dalam sebuah variabel data_barang_katalog lalu buat dictionary context yang menyimpan key-value dari semua objects of CatalogItem tersebut, nama author, dan NPM author. Terakhir function mereturn function render() dengan parameter request, file html katalog, dan dict context tadi.

2. Pada file urls.py di folder katalog, tambahkan list urlpatterns yang berisi function path dengan param show_katalog function. Selain itu pada urls.py di project_django, tambahkan path dengan param 'katalog/' dan include('katalog.urls') agar link /katalog terbaca saat diakses

3. Pertama loaddata dari file json dahulu agar data tersimpan di database lokal Django. setelah itu untuk menampilkan data ke user, edit katalog.html sehingga melooping semua data yang ada di database lokal lalu menampilkan data tersebut.

4. Pertama membuat app baru di heroku kemudian input API Key dan App Name ke dalam secret repository di github. Lakukan 3 magic word of Git yakni add, commit, push ke repository di github. Secara otomatis, github akan melakukan deployment ke Heroku dan websit app dapat diakses oleh semua orang.
