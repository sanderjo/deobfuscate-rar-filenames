# deobfuscate-rar-filenames
deobfuscate rar filenames

# Usage

```
./deobfuscate-rar-filenames.py
```
Result

```
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part10.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part11.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part12.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part13.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part14.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part15.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part16.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part17.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part18.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part19.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part1.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part20.rar
-rw-r--r-- 1 sander sander    3647 jul 26 20:28 blablabla.part21.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part2.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part3.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part4.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part5.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part6.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part7.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part8.rar
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 blablabla.part9.rar
```


# Convert plain rar files to obfuscated files

```
for f in *.rar; do echo "Processing $f file.."; mv $f `uuidgen` ; done
```

Result:
```
-rw-r--r-- 1 sander sander    3647 jul 26 20:28 00c1fc11-a79d-41be-b39d-8dcd7269e97f
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 2ba3fa2b-75af-445a-839e-276095362a50
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 3a1c27d8-6efd-45d0-9646-a04500702b80
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 3e18452d-d4f6-4d5d-830e-317e4c04ca50
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 4e2bbf59-a23c-4772-801b-48a3f535f7b0
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 5bb48125-310c-4ff2-8051-8490c2c64cfe
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 823cfc48-4fc1-4fd1-adcf-0d7633f0f20c
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 86181551-b56e-4003-93af-736d581f69ab
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 92704af6-be22-4f3f-b70e-28ecd66d32c0
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 92e531c6-b76b-4f99-a792-1cf24b62adb1
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 97bcd24e-cb20-4939-9e64-58e0ac9d01dd
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 98b4049f-457b-425f-a6fc-45d6571288b6
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 9dd7c045-7f62-4fbb-97c1-037c8dd058de
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 a66140e3-94a6-4294-94d3-8e3cfa88c629
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 ad98c8f7-9500-4c15-b977-df43f123ff55
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 d6f35903-6e92-45b1-8cbe-b17a6cc712d7
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 e449c102-9550-4a81-b97a-3bba6d929776
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 ed26d24e-6dc5-4d32-9cbb-962b798a1ddc
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 f21c283c-ba6d-41f4-9956-fd7d51cf9f3e
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 f6b642c0-68ee-410c-9fde-06168b5b7e0a
-rw-r--r-- 1 sander sander 5242880 jul 26 20:28 fc108630-348f-41af-bb6f-f0bdd150f776
```

