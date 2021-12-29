using System;

namespace Me_trying_to_learn_new_things
{
    class Program5
    {
        static void Main(string[] args)
        { 
          // Styling cause why not lol.
         Console.ForegroundColor = ConsoleColor.Blue;
  

         Random numberGen = new Random();

         // Declaring variables
          
         int roll1 = numberGen.Next(1, 7);
         
         int roll2 = numberGen.Next(1, 7);

         int attempts = 0;


         // Main
             
         Console.WriteLine("Press any key to roll the dice");

         while(roll1 != roll2) {

             Console.ReadKey();

             roll1 = numberGen.Next(1, 7);
             roll2 = numberGen.Next(1, 7);
             attempts++;

             Console.WriteLine("\nDice 1: " + roll1 + "\nDice 2: " + roll2);
         }
         Console.WriteLine("You got the two of a kind in " + attempts + " attempts!");
         
          // Closing line.
            Console.ReadKey();
        }
    }
}
