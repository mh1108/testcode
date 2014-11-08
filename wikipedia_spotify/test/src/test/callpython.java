package test;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;






public class callpython {
	
//	public void test() {
//		
////		ProcessBuilder pb = new ProcessBuilder("python","/Users/misaki/Documents/workspace/test/test.py");
////		Process p = pb.start();
////		try {
////			InputStream a = p.getInputStream();
////			System.out.println(a.toString());
////			int exitCode = p.waitFor();
////		} catch (InterruptedException e) {
////			// TODO Auto-generated catch block
////			e.printStackTrace();
////		}
//		String[] cmd = new String[] {"python", "/Users/misaki/Documents/workspace/test/test.py"};
//		Runtime a = Runtime.getRuntime();
//		
//	}
	
	
	
	public static void main(String []args){
		callpython a = new callpython();
		try {
			 a.run();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}


	
	
	public void run() {
		// TODO Auto-generated method stub
		String[] cmd = new String[] {"python2.7", "/Users/misaki/Documents/workspace/test/test.py", "Taylor Swift"};
		Runtime a = Runtime.getRuntime();
		String s = null;
		try {
			Process b = a.exec(cmd);
		
			BufferedReader stdInput = new BufferedReader(new 

	                InputStreamReader(b.getInputStream()));

	           BufferedReader stdError = new BufferedReader(new 

	                InputStreamReader(b.getErrorStream()));
	           BufferedWriter stdOutput = new BufferedWriter(new 

	        		   OutputStreamWriter(b.getOutputStream()));
	           while ((s = stdError.readLine()) != null) {

	                System.out.println(s);

	            }
	           while ((s = stdInput.readLine()) != null) {

	               System.out.println(s);
	               

	           }

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		


           // read the output

           
//		try {
//			// StreamGobbler errGobbler = new StreamGobbler(b.getErrorStream(), "Error");
//		    // StreamGobbler outputGobbler = new StreamGobbler(b.getInputStream(), "Output");
//		    // errGobbler.start();
//		    // outputGobbler.start();
//		} catch (IOException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
//		StringWriter writer = new StringWriter();
//		ScriptEngineManager manager = new ScriptEngineManager();
//	    ScriptContext context = new SimpleScriptContext();
//	    
//	    context.setWriter(writer); //configures output redirection
//	    ScriptEngine engine = manager.getEngineByName("python");
//	    try {
//			engine.eval(new FileReader("/Users/misaki/Documents/workspace/test/test.py"), context);
//		} catch (FileNotFoundException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		} catch (ScriptException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
//	    System.out.println(writer.toString()); 
	}
	

}
