# 🧰 Git Cheat Sheet

Полная шпаргалка по Git — инициализация, ветки, коммиты, откаты, push/pull.

---

## 📦 Инициализация репозитория

git init  
git add README.md  
git commit -m "first commit"  
git remote add origin https://github.com/stanruss/название.git  
git push -u origin master  

---

## 🔄 Получение изменений

git pull origin main --allow-unrelated-histories  
git pull origin  
git pull origin master  
git pull origin HEAD  

---

## ⬇️ Fetch (без merge)

git fetch origin  
git fetch origin master  
git fetch --all  

---

## 🕒 История и коммиты

git log --oneline                 # Все коммиты  
git show <commit_hash>            # Изменения в коммите  

---

## 📝 Работа с файлами

git add text.txt                  # Добавить файл  
git rm text.txt                   # Удалить файл  
git clean -f                      # Удалить untracked файлы  

---

## 📌 Статус и коммит

git status                        # Состояние репозитория  
git commit -a -m "Commit message" # Коммит всех отслеживаемых файлов  

---

## 🌿 Ветки

git branch                        # Список локальных веток  
git branch -a                     # Все ветки  
git branch some_branch            # Создать ветку  
git checkout some_branch          # Переключиться  
git checkout -b some_branch       # Создать и перейти  
git checkout -b some_branch origin/some_branch  # Подключить удалённую ветку  

---

## 🔀 Merge

git merge some_branch             # Слить ветку в текущую  

---

## 🗑️ Удаление веток

git branch -d some_branch         # Удалить после merge  
git branch -D some_branch         # Принудительно  
git push origin :branch-name      # Удалить удалённую ветку  

---

## 🚀 Push

git push origin                   # Запушить все ветки  
git push origin master            # Запушить master  
git push origin HEAD              # Запушить текущую ветку  
git push -f                       # Принудительно перезаписать историю  

---

## ⏪ Откат и восстановление

git checkout .                    # Восстановить все файлы  
git checkout <commit_hash>        # Перейти к коммиту  
git checkout master               # Вернуться в master  

---

## ♻️ Жёсткое восстановление из origin

⚠️ Удаляет локальные изменения

git reset --hard origin/master  
git reset --hard origin/<branch_name>  

---

## 🧨 Полный откат к коммиту

⚠️ Удаляет все коммиты после указанного

git reset --hard <commit_hash>  

---

## ✅ Полезно помнить

• git fetch — безопаснее, чем pull  
• git status — проверяй перед каждым commit  
• reset --hard и push -f — использовать осторожно  

---
