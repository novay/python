# API Samarinda (Py)
Library untuk menggunakan API Samarinda menggunakan Bahasa Python.

### Instalasi
```
pip install apisamarinda
```

### Contoh Penggunaan

```Python
from apisamarinda import api

# File api_auth.json bisa diunduh melalui halaman API Anda
request = api.ApiClient("./api_auth.json")

# Gunakan Endpoint yang Anda ingin tampilkan
result = request.result('API_URL')

# Tampilkan dalam bentuk JSON
result.json()
```

### TODO
Ini masih tahap uji coba karena bertepatan dengan tugas kuliah yang maksain pake Python.
- Saat ini hanya mendukung GET