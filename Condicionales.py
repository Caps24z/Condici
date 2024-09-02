package com.mycompany.actividadhoy;

import java.util.Scanner;

/**
*
* @author ESTUDIANTES
*/
public class Actividadhoy {

public static void main(String[] args) {
Scanner entrada = new Scanner(System.in);
//variable
String nombre,apellido;
int edad,sexo;
//entrada
System.out.println("Ingrese el nombre:");
nombre = entrada.nextLine();
System.out.println("ingrese apellido:");
apellido = entrada.nextLine();
System.out.println("ingrese edad:");
edad = entrada.nextInt();
System.out.println("ingrese el sexo:");
sexo = entrada.nextInt();

if (edad>0 && edad<=18){
System.out.println("ES MENOR DE EDAD");

}else{
System.out.println("ES MAYOR DE EDAD");

}
if (sexo==1 && sexo!=2){
System.out.println("ES MUJER");

}else{
System.out.println("ES HOMBRE");
}

}
}
