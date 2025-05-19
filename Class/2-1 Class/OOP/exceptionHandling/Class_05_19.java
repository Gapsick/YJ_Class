package exceptionHandling;


import java.io.IOException;
import java.security.cert.CertificateEncodingException;

class Bar {
    void prt() throws IOException {
        throw new IOException();
    }
}


public class Class_05_19 {
    public static void main(String[] args) /*throws Exception */{

        int pos = 0;
        try {
            System.out.println("t-1");

            if (pos == 0)
                throw new Exception();
            if (pos == 1)
                throw new CertificateEncodingException();
            if (pos == 2)
                throw new IOException();

        } catch (CertificateEncodingException e) {
            System.out.println("Exception:");
        } catch (IOException e) {
            System.out.println("Exception:");
        } catch (Exception e) {
            System.out.println("Exception:");
        }

        System.out.println("t-3");


    }
}
