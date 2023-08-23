# Question
class Question:
    def __init__(self,text, choices,answer):
        self.text = text 
        self.choices = choices
        self.answer = answer

    def chekAnswer(self,answer):
       return self.answer == answer
    
# Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    def getQuestion(self):
        return  self.questions[self.questionIndex]
    def displayQuestion(self):      
          question = self.getQuestion()
          print(f'Soru {self.questionIndex+1}: {question.text} ')
             
          for q in  question.choices:
              print('-'+q)

          answer = input('Enter your answer : ')
          self.guess(answer)
          self.loadQuestion()
    def guess(self,answer):
         question = self.getQuestion()
         if question.chekAnswer(answer):
             self.score +=1
         self.questionIndex +=1

    def loadQuestion(self): 
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
         self.displayPrograss()
         self.displayQuestion()

    def showScore(self):
     print('Score : ',self.score)


    def  displayPrograss(self):
         totalQuestion =len(self.questions)
         question_Number = self.questionIndex+1
         if question_Number > totalQuestion:
             print('Quiz over ..')
         else:
             print(f' Question {question_Number} of {totalQuestion} '.center(100,'*'))
        #   print(question.chekAnswer(answer))#AGAIN
    
q1 = Question('Which is the best programming language ? ',['C#','python','Java','Php'],'python')    
q2 = Question('Which is the most popular programming language ? ',['python','Java','C#','Php'],'python')     
q3 = Question('Which is most used programming language ? ',['Php','python','Java','C#'],'python')   
q4 = Question('Which is the most loved programming language ? ',['python','Java','C#','Php'],'python')     
q5 = Question('Which is the Easiest programming language ? ',['python','Java','C#','Php'],'python')     

# print(q1.chekAnswer('c#'))# output = False
# print(q1.chekAnswer('python'))# output = True
questions = [q1,q2,q3,q4,q5]
quiz = Quiz(questions)
# question = quiz.getQuestion()
quiz.loadQuestion()