Code Quality Assessment 

C# / Name: #07 Espiritu, Eliezer Marc #08 Intal, Kurt Ashe #09 Legaspi, Daniel Date: August 16, 2026

Problem

Finding the highest (maximum) number from a given list of numbers.

---

PseudoCode 1

```text
Algorithm FindMax1(numbers)

   max ← numbers[0]

   For i from 1 to length(numbers)-1

      If numbers[i] > max Then

         max ← numbers[i]

      EndIf

   EndFor

   Return max

EndAlgorithm

---

PseudoCode 2
```text
Algorithm FindMax2(numbers)

   For i from 0 to length(numbers)-1

      bigger ← true

      For j from 0 to length(numbers)-1

         If numbers[j] > numbers[i] Then

            bigger ← false

         EndIf

      EndFor

      If bigger = true Then

         Return numbers[i]

      EndIf

   EndFor

EndAlgorithm

---
