# SemanticTest
<h1>Код программа на python для вычисления расстояния между документами</h1>
В качестве документов взял определения математической статистики в разных источниках – Wikipedia, booksite, mathprofi, dic.academic; а алгебры – Wikipedia.
<br>
Кратко:<br>
Вычисление семантического расстояния между документами в векторной модели представления данных терм-документ.<br>
Пример для вычисления вручную<br>
Пусть дан эталон документа q (запрос), нужно сравнить его с документами в базе (doc1, doc2, doc3)<br>
![image](https://user-images.githubusercontent.com/50706625/117477944-a3d7ed80-af6f-11eb-9700-d22e272fb288.jpg)
<br>
С самого начала приводим все слова в документах к термам, по средствам стемминга и лемматизации, после чего подсчитываем сколько раз документ содержит термин (term frequency – tf ) <br>
![пример с изоморфизмомExcel](https://user-images.githubusercontent.com/50706625/117477479-185e5c80-af6f-11eb-8310-b74fa52db776.png)
После чего рассчитаем idf – обратная документальная частота, фукнция от величины, обратной к количеству документов, в которой встречается терм<br>
idf=log_2⁡(n/df),<br>
где n – количество документов,<br>
а df – частота в коллекции или число документов, в которые входит терм.<br>
Посчитаем вес конкретного терма t в документе doc, используя его частоту tf и idf по следующей формуле: tf-〖idf〗_(t,doc)=〖tf〗_(t,doc)*〖idf〗_t  <br>
Сам запрос (документ) q тоже приведем к векторному представлению таким же алгоритмом <br>
Посчитаем расстояние по косинусной мере сходства документов по следующей формуле:<br>
simCos(q,doc)=cos⁡(θ)=(q*doc)/(|(|q|)|*||doc||)=(∑_(i=1)^n▒〖(tf-〖idf〗_(q,i))*(tf-〖idf〗_(doc,i))〗)/(√(∑_(i=1)^n▒〖(tf-〖idf〗_(q,i))〗^2 )*√(∑_(i=1)^n▒〖(tf-〖idf〗_(doc,i))〗^2 ))
Результаты:<br>
simCos(q,doc1)≈0,7626<br>
simCos(q,doc2) ≈0.227<br>
simCos(q,doc3) ≈0.461<br>
На основе этого можно сказать, что документы q и doc1 семантически ближайшие документы.<br>
