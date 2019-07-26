# deobfuscate-rar-filenames
deobfuscate rar filenames

# Usage

```
./deobfuscate-rar-filenames.py
```


```
./deobfuscate-rar-filenames.py 
DEBUG:root:Log level is DEBUG
DEBUG:root:Handling 93c6ea9a-8034-4c6c-9516-ff1fa4d69d08
DEBUG:root:Renaming 93c6ea9a-8034-4c6c-9516-ff1fa4d69d08 to blablabla.part00003.rar
DEBUG:root:Handling 34f0b4f5-565c-44ee-b176-19acd8f86aa5
DEBUG:root:Renaming 34f0b4f5-565c-44ee-b176-19acd8f86aa5 to blablabla.part00015.rar
DEBUG:root:Handling 605ed5c2-31e7-40d7-855a-2ca84d693d11
DEBUG:root:Renaming 605ed5c2-31e7-40d7-855a-2ca84d693d11 to blablabla.part00008.rar
DEBUG:root:Handling 9d4b7e0c-e39f-444c-8d42-23ccc66cd5e3
DEBUG:root:Renaming 9d4b7e0c-e39f-444c-8d42-23ccc66cd5e3 to blablabla.part00014.rar
DEBUG:root:Handling 31dfbe5d-f03b-4163-8576-4e9bba39c129
DEBUG:root:Renaming 31dfbe5d-f03b-4163-8576-4e9bba39c129 to blablabla.part00017.rar
DEBUG:root:Handling b85bd293-00f9-43d1-a712-6806e8c735a2
DEBUG:root:Renaming b85bd293-00f9-43d1-a712-6806e8c735a2 to blablabla.part00016.rar
DEBUG:root:Handling c21a6b5d-a82e-4b0b-8d08-84c609e5e140
DEBUG:root:Renaming c21a6b5d-a82e-4b0b-8d08-84c609e5e140 to blablabla.part00013.rar
DEBUG:root:Handling d985bd84-2e92-4298-aea3-bc26e3894da0
DEBUG:root:Renaming d985bd84-2e92-4298-aea3-bc26e3894da0 to blablabla.part00012.rar
DEBUG:root:Handling 92538d66-586a-47fd-8647-f38020343201
DEBUG:root:Renaming 92538d66-586a-47fd-8647-f38020343201 to blablabla.part00001.rar
DEBUG:root:Handling eef6822f-5ddb-4c07-94a4-ed56dea7ef4f
DEBUG:root:Renaming eef6822f-5ddb-4c07-94a4-ed56dea7ef4f to blablabla.part00002.rar
DEBUG:root:Handling blabla.bin
DEBUG:root:Skipping (as not a rar file): blabla.bin
DEBUG:root:Handling cd9dab96-3440-4959-883f-ffda8f200d1f
DEBUG:root:Renaming cd9dab96-3440-4959-883f-ffda8f200d1f to blablabla.part00005.rar
DEBUG:root:Handling e6cc7884-e627-4a48-9b22-d6c859d16458
DEBUG:root:Renaming e6cc7884-e627-4a48-9b22-d6c859d16458 to blablabla.part00007.rar
DEBUG:root:Handling 34e55a8f-7c86-44b2-90fc-fa80977b9a66
DEBUG:root:Renaming 34e55a8f-7c86-44b2-90fc-fa80977b9a66 to blablabla.part00004.rar
DEBUG:root:Handling a3050e32-e39e-4a70-87ec-4cd555a1b14d
DEBUG:root:Renaming a3050e32-e39e-4a70-87ec-4cd555a1b14d to blablabla.part00011.rar
DEBUG:root:Handling d24830fa-f202-4616-a3f7-4bbcaa402028
DEBUG:root:Renaming d24830fa-f202-4616-a3f7-4bbcaa402028 to blablabla.part00009.rar
DEBUG:root:Handling 5c959007-bcd2-4b8d-b513-d48571953d4a
DEBUG:root:Renaming 5c959007-bcd2-4b8d-b513-d48571953d4a to blablabla.part00010.rar
DEBUG:root:Handling d93233c1-739c-4d0c-93e1-faf6bdb8648d
DEBUG:root:Renaming d93233c1-739c-4d0c-93e1-faf6bdb8648d to blablabla.part00006.rar

```
Result:
```
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00001.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00002.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00003.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00004.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00005.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00006.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00007.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00008.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00009.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00010.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00011.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00012.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00013.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00014.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00015.rar
-rw-r--r-- 1 sander sander 6291456 jul 26 21:21 blablabla.part00016.rar
-rw-r--r-- 1 sander sander 4197322 jul 26 21:21 blablabla.part00017.rar
```


# FWIW For testing: Convert plain rar files to obfuscated files

```
fallocate  -l100m blabla.bin
rar a something -v6m -m0 *
for f in *.rar; do echo "Processing $f file.."; mv $f `uuidgen` ; done
```

Result:
```
total 204812
drwxr-xr-x 2 sander sander      4096 jul 26 21:21 ./
drwxr-xr-x 4 sander sander      4096 jul 26 21:21 ../
-rw-r--r-- 1 sander sander   4197322 jul 26 21:21 31dfbe5d-f03b-4163-8576-4e9bba39c129
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 34e55a8f-7c86-44b2-90fc-fa80977b9a66
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 34f0b4f5-565c-44ee-b176-19acd8f86aa5
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 5c959007-bcd2-4b8d-b513-d48571953d4a
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 605ed5c2-31e7-40d7-855a-2ca84d693d11
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 92538d66-586a-47fd-8647-f38020343201
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 93c6ea9a-8034-4c6c-9516-ff1fa4d69d08
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 9d4b7e0c-e39f-444c-8d42-23ccc66cd5e3
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 a3050e32-e39e-4a70-87ec-4cd555a1b14d
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 b85bd293-00f9-43d1-a712-6806e8c735a2
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 c21a6b5d-a82e-4b0b-8d08-84c609e5e140
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 cd9dab96-3440-4959-883f-ffda8f200d1f
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 d24830fa-f202-4616-a3f7-4bbcaa402028
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 d93233c1-739c-4d0c-93e1-faf6bdb8648d
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 d985bd84-2e92-4298-aea3-bc26e3894da0
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 e6cc7884-e627-4a48-9b22-d6c859d16458
-rw-r--r-- 1 sander sander   6291456 jul 26 21:21 eef6822f-5ddb-4c07-94a4-ed56dea7ef4f

```

