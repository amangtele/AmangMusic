#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>Admin Commands:</u>**

**c** adalah singkatan dari pemutaran saluran.

/pause atau /cpause - Menjeda musik yang sedang diputar.
/resume atau /cresume- Melanjutkan musik yang dijeda.
/mute atau /cmute- Mematikan musik yang diputar.
/unmute atau /cunmute- Mengaktifkan musik yang dimatikan.
/skip atau /cskip- Lewati musik yang sedang diputar.
/stop atau /cstop- Menghentikan pemutaran musik.
/shuffle atau /cshuffle- Secara acak mengacak daftar putar yang antri.
/seek atau /cseek - Teruskan Cari musik sesuai durasi Anda
/seekback atau /cseekback - Mundur Mencari musik sesuai durasi Anda
/restart - Mulai ulang bot untuk obrolan Anda .


✅<u>**Specific Skip:**</u>
/skip atau /cskip [Nomor(contoh: 3)]
     - Melompati musik ke nomor antrian yang ditentukan. Contoh: /skip 3 akan melewatkan musik ke musik antrian ketiga dan akan mengabaikan musik 1 dan 2 dalam antrian.

✅<u>**Loop Play:**</u>
/loop or /cloop [enable/disable] or [Angka antara 1-10] 
    - Saat diaktifkan, bot memutar musik yang sedang diputar menjadi 1-10 kali pada obrolan suara. Default ke 10 kali.

✅<u>**Auth Users:**</u>
Pengguna Auth dapat menggunakan perintah admin tanpa hak admin di obrolan Anda.

/auth [Username] - Tambahkan pengguna ke AUTH LIST grup.
/unauth [Username] - Hapus pengguna dari AUTH LIST grup.
/authusers - Periksa DAFTAR AUTH grup."""


HELP_2 = """✅<u>**Play Commands:**</u>

Perintah yang tersedia = play , vplay , cplay

Perintah ForcePlay = playforce , vplayforce , cplayforce

**c** singkatan dari pemutaran di Chanell.
**v** singkatan dari pemutaran video.
**force** singkatan dari force play.

/play or /vplay or /cplay  - Bot akan mulai memainkan kueri yang Anda berikan di obrolan suara atau Streaming tautan langsung di obrolan suara.

/playforce or /vplayforce or /cplayforce -  **Force Play** menghentikan trek yang sedang diputar di obrolan suara dan mulai memutar trek yang dicari secara instan tanpa mengganggu/clearing queue.

/channelplay [Chat username or id] or [Disable] - Hubungkan saluran ke grup dan streaming musik di obrolan suara saluran dari grup Anda.


✅**<u>Bot's Server Playlists:</u>**
/playlist  - Periksa Daftar Putar Tersimpan Anda Di Server.
/deleteplaylist - Hapus semua musik yang disimpan di daftar putar Anda
/play  - Mulai mainkan Daftar Putar Tersimpan Anda dari Server."""


HELP_3 = """✅<u>**Bot Commands:**</u>

/stats - Dapatkan 10 Trek Global Stats Teratas, 10 Pengguna Bot Teratas, 10 Obrolan Teratas di bot, 10 Teratas Dimainkan dalam obrolan, dll..

/sudolist - Periksa Sudo Pengguna Cilik Music Bot

/lyrics [Music Name] - Mencari Lirik untuk Musik tertentu di web.

/song [Track Name] or [YT Link] - Unduh lagu apa pun dari youtube dalam format mp3 atau mp4.

/player -  Dapatkan Panel Bermain interaktif.

**c** stands for channel play.

/queue or /cqueue- Check Queue List of Music."""

HELP_4 = """✅<u>**Extra  Commands:**</u>
/start - Mulai Bot Musik.
/help - Dapatkan Menu Helper Perintah dengan penjelasan rinci tentang perintah.
/ping- Ping Bot dan periksa statistik Ram, Cpu, dll dari Bot.

✅<u>**Group Settings:**</u>
/settings - Dapatkan pengaturan grup lengkap dengan tombol sebaris

🔗 **Options in Settings:**

1️⃣ Anda dapat mengatur **Kualitas Audio** yang ingin Anda streaming di obrolan suara.

2️⃣ Anda dapat mengatur **Kualitas Video** yang ingin Anda streaming di obrolan suara.

3️⃣ **Pengguna Auth**:- Anda dapat mengubah mode perintah admin dari sini ke semua orang atau hanya admin. Jika semua orang, siapa pun yang ada di grup Anda dapat menggunakan perintah admin (seperti /skip, /stop dll)

4️⃣ **Mode Bersih:** Saat diaktifkan, hapus pesan bot setelah 5 menit dari grup Anda untuk memastikan obrolan Anda tetap bersih dan baik.

5️⃣ **Perintah Bersih** : Saat diaktifkan, Bot akan segera menghapus perintah yang dijalankannya (/play, /pause, /shuffle, /stop dll).

6️⃣ **Pengaturan Putar:**

/playmode - Dapatkan panel pengaturan pemutaran lengkap dengan tombol di mana Anda dapat mengatur pengaturan pemutaran grup Anda.

<u>Opsi dalam mode putar:</u>

1️⃣ **Mode Pencarian** [Langsung atau Sebaris] - Mengubah mode pencarian Anda saat Anda memberikan mode /play.

2️⃣ **Perintah Admin** [Semua Orang atau Admin] - Jika semua orang, siapa pun yang hadir di grup Anda akan dapat menggunakan perintah admin (seperti /skip, /stop dll)

3️⃣ **Tipe Putar** [Semua Orang atau Admin] - Jika admin, hanya admin yang ada di grup yang dapat memutar musik di obrolan suara."""

HELP_5 = """🔰**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Nama pengguna atau Balas ke pengguna]
/delsudo [Nama pengguna atau Balas ke pengguna]

🛃**<u>HEROKU:</u>**
/usage - Dyno Usage.

🌐**<u>CONFIG VARS:</u>**
/get_var - Dapatkan config var dari Heroku atau .env.
/del_var - Hapus semua var di Heroku atau .env.
/set_var [Var Name] [Value] - Atur Var atau Perbarui Var di heroku atau .env. Pisahkan Var dan Nilainya dengan spasi.

🤖**<u>BOT COMMANDS:</u>**
/reboot - Nyalakan ulang Bot Anda.
/update - Perbarui Bot.
/speedtest - Periksa kecepatan server
/maintenance [aktifkan / nonaktifkan]
/logger [aktifkan / nonaktifkan] - Bot mencatat kueri yang dicari di grup logger.
/get_log [Jumlah Baris] - Dapatkan log bot Anda dari heroku atau vps. Bekerja untuk keduanya.
/autoend [enable|disable] - Aktifkan Auto stream end setelah 3 menit jika tidak ada yang mendengarkan.

📈**<u>STATS COMMANDS:</u>**
/activevoice - Periksa obrolan suara aktif di bot.
/activevideo - Periksa panggilan video aktif di bot.
/stats - Periksa Statistik Bot

⚠️**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Daftar hitam obrolan apa pun dari menggunakan Bot Musik
/whitelistchat [CHAT_ID] - Daftar putih obrolan apa pun yang masuk daftar hitam dari menggunakan Bot Musik
/blacklistedchat - Periksa semua obrolan yang masuk daftar hitam.

👤**<u>BLOCKED FUNCTION:</u>**
/block [Nama Pengguna atau Balas ke pengguna] - Mencegah pengguna menggunakan perintah bot.
/unblock [Nama Pengguna atau Balas ke pengguna] - Hapus pengguna dari Daftar Blokir Bot.
/blockedusers - Periksa Daftar Pengguna yang diblokir

👤**<u>GBAN FUNCTION:</u>**
/gban [Nama Pengguna atau Balas ke pengguna] - Gban pengguna dari obrolan yang dilayani bot dan hentikan dia menggunakan bot Anda.
/ungban [Nama Pengguna atau Balas ke pengguna] - Hapus pengguna dari Daftar gbanned Bot dan izinkan dia menggunakan bot Anda
/gbannedusers - Periksa Daftar Pengguna Gbanned

🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Jumlah Obrolan] - Tetapkan Jumlah Obrolan maksimum yang diizinkan untuk Panggilan Video dalam satu waktu. Default untuk 3 obrolan.
/videomode [download|m3u8] - Jika mode unduh diaktifkan, Bot akan mengunduh video alih-alih memutarnya dalam bentuk M3u8. Secara default ke M3u8. Anda dapat menggunakan mode unduhan saat kueri apa pun tidak diputar dalam mode m3u8.

⚡️**<u>PRIVATE BOT FUNCTION:</u>**
/authorize[CHAT_ID] - Izinkan obrolan untuk menggunakan bot Anda.
/unauthorize [CHAT_ID] - Melarang obrolan menggunakan bot Anda.
/authorized - Periksa semua obrolan bot Anda yang diizinkan.

🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Pesan atau Balas Pesan] - Menyiarkan pesan apa pun ke Obrolan yang Dilayani Bot.

<u>options for broadcast:</u>
**-pin** : Ini akan menyematkan pesan Anda
**-pinloud** : Ini akan menyematkan pesan Anda dengan pemberitahuan keras
**-user** : Ini akan menyiarkan pesan Anda ke pengguna yang telah memulai bot Anda.
**-assistant** : Ini akan menyiarkan pesan Anda dari akun asisten bot Anda.
**-nobot** : Ini akan memaksa bot Anda untuk tidak menyiarkan pesan

**Contoh:** `/broadcast -user -assistant -pin Halo Pengujian`

"""
