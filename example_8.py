class Question():
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answers=answer
    def checkAnswer(self,answerUs):
        return self.answers == answerUs

class Quiz():
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.index=0
    def getQuestion(self):
        return self.questions[self.index]
    
    def displayQuestion(self):
        question=self.getQuestion()
        print(f'Soru {self.index+1}: {question.text}')

q1=Question('En iyi programlama dili hangisidir? ',['C#','python','Javascript','Java'],'python')
q2=Question('En popüler programlama dili hangisidir? ',['python','Javascript','Java','C#'],'python')
q3=Question('En çok kazandıran programlama dili hangisidir? ',['python','Javascript','C#','Java'],'python')

questions=[q1,q2,q3]# Sorular class array olarak listelenmiştir.

quiz1=Quiz(questions)
quiz1.displayQuestion()

