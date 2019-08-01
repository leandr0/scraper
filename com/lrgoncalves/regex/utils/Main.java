import java.util.regex.*;
import java.io.*; 
import java.util.Scanner; 

class Main
{
  public static void main(String[] args)
  {
  
    try{	 
    String txt = readFile(args[0]);		
    //String txt="publicIdentifier\":\"leandrorgoncalves\"";

    String re1=".*?";	// Non-greedy match on filler
    String re2="(?:[a-z][a-z0-9_]*)";	// Uninteresting: var
    String re3=".*?";	// Non-greedy match on filler
    String re4="((?:[a-z][a-z0-9_]*))";	// Variable Name 1

    Pattern p = Pattern.compile("(publicIdentifier&quot;:&quot;)([-a-zA-Z0-9]+)(&quot;)"); 
//Pattern.compile(re1+re2+re3+re4,Pattern.CASE_INSENSITIVE | Pattern.DOTALL);
    Matcher m = p.matcher(txt);
    while (m.find())
    {
        String var1=m.group(2);
        if(var1.equals("UNKNOWN")){
		break;
        }
        System.out.print("https://www.linkedin.com/in/"+var1.toString()+"/"+"\n");
    }
   }catch(Exception ex){
     System.err.println(ex);
  }
}

 private static String readFile(String pathname) throws IOException {

    File file = new File(pathname);
    StringBuilder fileContents = new StringBuilder((int)file.length());        

    try (Scanner scanner = new Scanner(file)) {
        while(scanner.hasNextLine()) {
            fileContents.append(scanner.nextLine() + System.lineSeparator());
        }
        return fileContents.toString();
    }
}

}

//-----
// This code is for use with Sun's Java VM - see http://java.sun.com/ for downloads. 
//
// Paste the code into a new java application or a file called 'Main.java'
//
// Compile and run in Unix using:
// # javac Main.java 
// # java Main 
//
