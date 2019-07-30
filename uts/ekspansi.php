<?php
// Dekripsi
// Kalimat
$cipher = "25an ekniktan asardan riptografikan";
echo 'Cipher: ' .  $cipher;
echo "<br>";
echo 'Plaintext: ';
// Mengubah kalimat menjadi array dan menghapus spasi
$array = explode(" ", $cipher);

// Looping sepanjang jumlah array
for ($i = 0; $i < count($array); $i++) {
    // Jika index terakhir dari array adalah huruf n
    if ($array[$i][-1] == 'n') {
        // variabel before untuk mengambil huruf/angka sebelum huruf 'an'
        $before = $array[$i][strlen($array[$i]) - 3];
        // menampilkan variabel before di awal dan menampilkan semua huruf/angka sebelum 'an'
        echo $before . substr($array[$i], 0, -3) . " ";
    }
    // jika index terakhir dari array adalah huruf i 
    else if ($array[$i][-1] == 'i') {
        // variabel before untuk mengambil huruf/angka sebelum huruf 'i'
        $before = $array[$i][strlen($array[$i]) - 2];
        // menampilkan variabel before di awal dan menampilkan semua huruf/angka sebelum 'i'
        echo $before . substr($array[$i], 0, -2) . " ";
    }
}

// import java.io.*;
// import java.util.*;
// import java.util.Scanner;
// public class JavaApplication4 {
//     public static void main(String args[])throws IOException
// 	{
// 		Scanner s=new Scanner(System.in);
// 		int lkey,i,j,l,r,q,row=0,col=0;

// 		System.out.println("Enter length of key");
// 		lkey=s.nextInt();
// 		int key[]=new int[lkey];
// 		System.out.println("Enter key");

// 		for(i=0;i < key.length;i++)
// 		{
//                        key[i]=s.nextInt();
// 		}

// 		System.out.println("Enter text to be sent without spaces");
// 		String text;
// 		text=s.next();
// 		l=text.length();
// 		q=l/lkey;  //3
// 		r=l%lkey;  //1

// 		if(r!=0)
// 		{
// 			q++;
// 		}


// 			char c[][]=new char[q][lkey];
// 			char t[][]=new char[q][lkey];
// 			for(i=0;i < l;i++)
// 			{
// 				if(col==lkey)
// 				{
// 					row++;
// 					col=0;
// 				}
// 				c[row][col]=text.charAt(i);
// 				col++;
// 			}
// System.out.println();
		

// 		System.out.println("Cipher in matrix form:");
// 		for(i=0;i < q;i++)
// 		{
// 			for(j=0;j < lkey;j++)
// 			{
// 				System.out.print(c[i][j]  + " ");
// 			}
// 			System.out.println();
// 		}
// 		System.out.println();

// 		System.out.println("Cipher to be sent:");
		
// 		for(i=0;i<key.length;i++)
// 		{
// 			for(j=0;j<q;j++)
// 			{ 
// 				System.out.print(c[j][i]);

// 			}
			
// 		}
// 		   System.out.println();
// 		   System.out.println();
//              System.out.println("After deciphering:");
//          for(i=0;i < q;i++)
// 		{
// 			for(j=0;j < lkey;j++)
// 			{
// 				System.out.print(c[i][j]);
// 			}
			
// 		}
		
// 	}
// }
