import java.io.*;
import java.lang.Number.*;

/*
	Programa que calcula l'exponenciaci? r?pida per a calcular a^z mod n
	Author: Gerard Farr?s i Ballabriga (gfarrasb@uoc.edu)
*/

public class exp_rapid {


  public static void main (String[] args) throws Exception {

  boolean endavant = true;

  if (args.length < 3) {
  	System.out.println("Usage: exp_rapid a z n\nPer a calcular: a^z mod n");
	endavant = false;
  }


  if(endavant) {

	  	int a1 = (new java.lang.Integer(args[0])).intValue();
  		int z1 = (new java.lang.Integer(args[1])).intValue();
  		int n = (new java.lang.Integer(args[2])).intValue();
  		int x = 1;

  		while (z1 != 0) {

			while ((z1 % 2) == 0)

			{

			z1 = z1/2;
			a1 = (a1 * a1) % n;

			}

		z1 = z1 - 1;
		x = (x * a1) % n;

  		}

  System.out.println("Resultat de: " + args[0] + "^" + args[1] + " mod " + args[2] + "=" + x);


}
}
}
