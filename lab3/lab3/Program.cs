/*3. Особа має функцію корисності U(x) = x^(1/2) і вона обирає нове місце
роботи, виходячи з двох альтернатив. У першому випадку її невизначена
заробітна платня може становити 1000 гр. од. з ймовірністю 0,5 або 3000 гр.
од. з тією самою ймовірністю. В іншому місці їй пропонується детермінована 
заробітна платня 2000 гр. од. Яке місце роботи доцільно обрати цій особі?
 */


using System;

class Program
{
    static void Main()
    {
        // невизначена зарплата
        double prob1 = 0.5;
        double salary1Low = 1000;
        double salary1High = 3000;

        // очікувана корисність для невизначеної роботи
        double expectedUtility1 = prob1 * Math.Sqrt(salary1Low) + prob1 * Math.Sqrt(salary1High);

        // детермінована зарплата
        double salary2 = 2000;
        double utilitySalary2 = Math.Sqrt(salary2);

        // обчислення детермінованого еквівалента
        double deterministicEquivalent = Math.Pow(expectedUtility1, 2);
        double riskPremium = salary2 - deterministicEquivalent; //премія за ризик

        string preferredJob = expectedUtility1 > utilitySalary2 ? "Option 1 (Uncertain job)" : "Option 2 (Deterministic job)";

        // Виведення результатів
        Console.WriteLine($"Expected utility of Option 1: {expectedUtility1}");
        Console.WriteLine($"Utility of Option 2: {utilitySalary2}");
        Console.WriteLine($"Deterministic equivalent: {deterministicEquivalent}");
        Console.WriteLine($"Risk discount: {riskPremium}");
        Console.WriteLine($"Preferred job: {preferredJob}");
    }
}