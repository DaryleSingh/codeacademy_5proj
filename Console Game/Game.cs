using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {


  public static new void  UpdatePosition(string keypressed, out int changeinx,out int changeiny) {

changeinx=0;
changeiny=0;

switch(keypressed) {
 case "LeftArrow":
       changeinx=changeinx -1 ;
       break;
 case "RightArrow":
       changeinx=changeinx +1 ;
       break;
 case "UpArrow":
       changeiny=changeiny - 1;
       break;
 case "DownArrow":
       changeiny=changeiny + 1;
       break;
}

    }//UpdatePosition

 public static new char UpdateCursor(string keypressed) {

switch(keypressed) {
 case "LeftArrow":
       return '<';
       break;
 case "RightArrow":
       return '>';
       break;
 case "UpArrow":
       return '^';
       break;
 case "DownArrow":
       return 'v';
       break;
 default:
       return 'v';
    break;
}


 }   
    

public static new int KeepInBounds(int cordinate,int maxvalue)  {

  if (cordinate <0) { 
    return 0;
  } else if (cordinate > (maxvalue-1))
  { 
    return maxvalue-1;
  } else {
    return cordinate;
  }


}

public static new bool DidScore(int charx,int chary,int fruitx,int fruity)  {

  if((charx==fruitx) && (chary==fruity)) {
    return true;
  } else {
    return false;
  }

}



  }  //class Game : SuperGame
}