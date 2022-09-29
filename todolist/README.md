# Assignment 4 PBP

Nama  : Erlangga Ahmad Khadafi

NPM   : 2106750894

Kelas : PBP-B

## LINK

Main Page           : https://tugas2dafi.herokuapp.com/

Katalog Page        : https://tugas2dafi.herokuapp.com/katalog/

MyWatchlist Page    : https://tugas2dafi.herokuapp.com/mywatchlist/

ToDoList Page       : https://tugas2dafi.herokuapp.com/todolist/


## Apa kegunaan {% csrf_token %} pada elemen <form>?
`{% csrf_token %}` berfungsi melindungi website dari serangan Cross-site request forgery (CSRF) dengan cara men-generate token unik untuk setiap session pengguna. Setiap pengguna mengirimkan request, CSFR token juga akan dikirimkan. Jika CSFR tokennya tidak valid (CSFR token pada session dan request-nya tidak sama), maka request tidak akan di-execute. \
Apabila tidak ada `{% csrf_token %}` pada elemen <form>, Cross-site request forgery (CSRF) akan lebih rentan terjadi. Dalam hal ini, attacker akan lebih mudah untuk melakukan modifikasi pada <form> seperti melakukan request POST karena tidak ada pengecekan CSFR token untuk setiap session dan request-nya.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})?
Elemen `<form>` dapat dibuat secara manual di file html. Sebagai contoh, pada `login.html`, `<form>` dibuat secara manual. Hal tersebut dilakukan dengan memanfaatkan tag `<input>` yang ada di HTML dengan `type` yang disesuaikan dengan kebutuhan, seperti `'text'` untuk textfield. `'password'` untuk field password, `'submit'` untuk button submit, dll.


## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika pengguna melakukan submisi form, maka akan dibuat _instance_ dari TaskForm yang ada di `forms.py` sesuai dengan input yang dimasukkan pengguna. 
Lalu akan terjadi pengecekan, apabila form tersebut valid, maka semua attribut yang ada pada model akan disesuaikan dengan input pengguna. Data tersebut disimpan ke databse saat
pemanggilan method `.save()`. Saat di-_redirect_ ke halaman HTML, data akan ditampilkan melalui _for loop_ setiap atribut yang ada pada model.

## Implementasi
#### 1. Membuat app baru bernama todolist di project tugas Django yang sudah ada

#### 2. Menambahkan path todolist di `urls.py` pada folder project_django dan meanmbahkan app todolist di `INSTALLED_APP`

#### 3. Membuat model Task yang memiliki atribut user, date, title, dan description

#### 4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.

##### - Membuat method untuk menampilkan dan menghandle page login, registrasi, dan logout di `views.py`
##### - Menambahkan path untuk menghandle itu ke `urls.py` di folder todolist


#### 5. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.

##### - Membuat folder templates untuk menyimpan file `.html` di folder todolist
##### - Membuat file html untuk ditampilkan kepada pengguna. Implementasi formnya menggunakan auto generated form dan manual menggunakan tag `<input>`.

#### 6. Deployment ke Heroku dengan push ke repository Github

#### 7. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task