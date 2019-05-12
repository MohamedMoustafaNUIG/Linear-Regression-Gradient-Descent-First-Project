import java.util.*;
import java.io.*;
public class Multivariate_LinearRegression
{
    private static double theta0,theta1,theta2,theta3;//parameters

    private static ArrayList<Double> expectedOutput=new ArrayList();//output,sepal length

    private static ArrayList<Double> attribute1=new ArrayList();//input1,sepal width
    private static ArrayList<Double> attribute2=new ArrayList();//input2,petal length
    private static ArrayList<Double> attribute3=new ArrayList();//input3,petal width

    private static double accuracy;

    public static void main(String[] args)
    {
        theta0=theta1=theta2=theta3=0;
        accuracy=0;
        try{
            BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\...\\iris.txt"));
            for(int i=0;i<50;i++)
            {
                String[] str=br.readLine().split(" ");
                expectedOutput.add(Double.parseDouble(str[0]));
                attribute1.add(Double.parseDouble(str[1]));
                attribute2.add(Double.parseDouble(str[2]));
                attribute3.add(Double.parseDouble(str[3]));
            }

            gradientDescent();
            testOnTen();
            System.out.println(accuracy);
        }
        catch (FileNotFoundException e) {
            System.out.println(e);
        } catch (IOException e) {
            System.out.println(e);
        }

    }

    public static double costFunction()
    {
        double m = 50.0;

        double multBy = 1.0/(2*m);
        double sum=0;

        double temp=0;

        for(int i=0;i<40;i++)
        {
            temp+=theta0;
            temp+=theta1*attribute2.get(i);
            temp-=attribute3.get(i);
            temp=Math.pow(temp,2);
            sum+=temp;
            temp=0;
        }

        return (multBy*sum);
    }

    public static double thetaPartialDerivative(int j)
    {
        double multBy=1.0/40;

        double sum=0;
        double temp=0;

        for(int i=0;i<40;i++)
        {
            temp+=theta0;
            temp+=theta1*attribute1.get(i);
            temp+=theta2*attribute2.get(i);
            temp+=theta3*attribute3.get(i);
            temp-=expectedOutput.get(i);
            switch(j)
            {
                case 0:break;
                case 1:temp*=attribute1.get(i);break;
                case 2:temp*=attribute1.get(i);break;
                case 3:temp*=attribute1.get(i);break;
            }
            sum=sum+temp;
            temp=0;

        }

        return (multBy*sum);
    }

    public static void gradientDescent()
    {
        double alpha = 0.08;

        double theta0After=theta0+1;
        double theta1After=theta1+1;
        double theta2After=theta2+1;
        double theta3After=theta3+1;

        while(theta0After!=theta0 && theta1After!=theta1
                && theta2After!=theta2 && theta3After!=theta3)
        {
            theta0=theta0After;
            theta1=theta1After;
            theta2=theta2After;
            theta3=theta3After;

            theta0After=theta0-(alpha*thetaPartialDerivative(0));
            theta1After=theta1-(alpha*thetaPartialDerivative(1));
            theta2After=theta2-(alpha*thetaPartialDerivative(2));
            theta3After=theta3-(alpha*thetaPartialDerivative(3));

            //To check whether partial derivatives are converging or diverging
	    /*
            System.out.println(thetaPartialDerivative(0));
            System.out.println(thetaPartialDerivative(1));
            System.out.println(thetaPartialDerivative(2));
            System.out.println(thetaPartialDerivative(3));
	    */
        }
    }

    public static void testOnTen()
    {
        double sum=0;
        for(int i=40;i<50;i++)
        {
            double prediction=
                    theta0+(theta1*attribute1.get(i))+(theta2*attribute2.get(i))+(theta3*attribute3.get(i));
            sum+=Math.min(prediction,expectedOutput.get(i))/Math.max(prediction,expectedOutput.get(i));
        }

        accuracy=(sum/10)*100;
    }
}


