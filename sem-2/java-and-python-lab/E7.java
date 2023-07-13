/* 
 * Student Name - Aakash Jain.
 * Roll No. - 222010019.
 * Lab Experiment No. 7 - UI widget factory needs to be designed. There are two types of input builders: TextInputBuilder, which accepts all characters and NumericInputBuilder, which accepts only digits..
*/

import java.io.*;

class UserInputBuilder {

    public static class TextInputBuilder {

        static StringBuffer str = new StringBuffer();

        public void add(char c) {
            str.append(c);
        }

        public String getValue() {
            return str.toString();
        }

    }

    public static class NumericInputBuilder extends TextInputBuilder{

        static StringBuffer str = new StringBuffer();

        @Override
        public void add(char c) {
            if (Character.isDigit(c)) {
                str.append(c);
            }
        }

        @Override
        public String getValue() {
            return str.toString();
        }
    }

    public static class OddNumericInputBuilder extends NumericInputBuilder {

        StringBuffer str = new StringBuffer();

        @Override
        public void add(char c) {
            if (Character.isDigit(c) && Character.getNumericValue(c) % 2 == 1) {
                str.append(c);
            }
        }

        @Override
        public String getValue() {
            return str.toString();
        }
    }

    public static class EvenNumericInputBuilder extends NumericInputBuilder {

        StringBuffer str = new StringBuffer();

        @Override
        public void add(char c) {
            if (Character.isDigit(c) && Character.getNumericValue(c) % 2 == 0) {
                str.append(c);
            }
        }

        @Override
        public String getValue() {
            return str.toString();
        }
    }

    public static void main(String[] args) {
        TextInputBuilder txt = new TextInputBuilder();
        txt.add('J');
        txt.add('A');
        txt.add('V');
        txt.add('A');
        System.out.println("TextInputBuilder: " + txt.getValue());

        TextInputBuilder num = new NumericInputBuilder();
        num.add('4');
        num.add('2');
        num.add('.');
        System.out.println("NumericInputBuilder: " + num.getValue());

        TextInputBuilder oddNum = new OddNumericInputBuilder();
        oddNum.add('1');
        oddNum.add('2');
        oddNum.add('3');
        oddNum.add('4');
        oddNum.add('5');
        System.out.println("OddNumericInputBuilder: " + oddNum.getValue());

        TextInputBuilder evenNum = new EvenNumericInputBuilder();
        evenNum.add('1');
        evenNum.add('2');
        evenNum.add('3');
        evenNum.add('4');
        evenNum.add('5');
        System.out.println("EvenNumericInputBuilder: " + evenNum.getValue());
    }
}
