using System;

namespace Me_trying_to_learn_new_things
{
    class Program2
    {
        static void Main(string[] args)
        { 
          // Styling cause why not lol.
         Console.ForegroundColor = ConsoleColor.Blue;

          // The main conversation.

           Console.WriteLine("Hello, what's your name?");

            string userName = Console.ReadLine();
   
            Console.WriteLine("Hello " + userName + ", Nice to meet you :-)");

            Console.WriteLine("What's your favorite color?");

            string userColor = Console.ReadLine();

            Console.WriteLine("Oh nice! \nMine is " + userColor + " too!");

            Console.WriteLine("What's your favorite hobby?");

            string userHobby = Console.ReadLine();

            Console.WriteLine("Yeah, " + userHobby + " is a cool hobby.");

            Console.WriteLine("Where do you live?");

            string userHome = Console.ReadLine();

            Console.WriteLine("Oh cool, " + userHome + " is a cool place! \nI live in your computer.");

            Console.WriteLine("What's your favourite food?");

            string userFood = Console.ReadLine();

            Console.WriteLine("It's always nice to eat " + userFood + ".");

            Console.WriteLine("Press any key to escape.");

          // Closing line
            Console.ReadKey();
        }
    }
}