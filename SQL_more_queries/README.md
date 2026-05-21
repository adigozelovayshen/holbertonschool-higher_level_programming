# SQL - More Queries

Bu qovluqdakı skriptlər MySQL üzərində istifadəçi icazələri, təhlükəsizlik tənzimləmələri və inkişaf etmiş sorğuları əhatə edir.

## Tapşırıq 0: My privileges!
`0-privileges.sql` skripti serverdəki `user_0d_1` və `user_0d_2` istifadəçilərinin malik olduğu bütün icazələri (grants) siyahılayır.

### İstifadə Qaydası:
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
