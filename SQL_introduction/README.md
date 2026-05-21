# SQL Introduction

Bu qovluq **Holberton School**-un Machine Learning proqramı çərçivəsində keçirilən **SQL (Structured Query Language)** modulu üçün tapşırıqları və skriptləri ehtiva edir. Layihənin məqsədi Relyasiya Verilənlər Bazası İdarəetmə Sistemləri (RDBMS) və xüsusilə **MySQL** ilə işləmək, verilənlər üzərində fundamental əməliyyatları (DDL və DML) öyrənməkdir.

---

## 📌 Fundamental Anlayışlar

* **SQL (Structured Query Language)**: Verilənlər bazası ilə ünsiyyət qurmaq, sorğular yazmaq və məlumatları idarə etmək üçün standart dildir.
* **Relyasiya Verilənlər Bazası (Relational Database)**: Məlumatların bir-biri ilə əlaqəli cədvəllər (tables), sətirlər (records/rows) və sütunlar (columns) şəklində mütəşəkkil təşkil olunduğu bazadır. Axtarışın optimallaşdırılması üçün indekslərdən (indexes) istifadə edir.
* **DDL (Data Definition Language)**: Bazanın strukturunu təyin edən əmrlər (, , ).
* **DML (Data Manipulation Language)**: Cədvəlin daxilindəki məlumatları manipulyasiya edən əmrlər (, , , ).

---

## 🛠️ Tapşırıqlar Siyahısı

| Fayl Adı | Tapşırığın Təsviri |
| :--- | :--- |
| **** | MySQL serverində mövcud olan bütün verilənlər bazalarını siyahılayır. |

---

## 🚀 Skriptlərin İşə Salınması

Yazılmış SQL skriptlərini terminal vasitəsilə MySQL serverində aşağıdakı komanda ilə test edə bilərsiniz:

```bash
cat <fayl_adı.sql> | mysql -hlocalhost -uroot -p
```
