import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class FileLoader {
    private String filePath;
    private String fileContent = "";

    FileLoader(String filePath) {
        this.filePath = filePath;
        loadFile();
    }

    private void loadFile() {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                fileContent += line + "\n";
            }
            System.out.println("파일 로드 성공!");
        } catch (IOException e) {
            System.out.println("파일 로드 실패: " + e.getMessage());
        }
    }

    // 파일 내용 출력
    void printFileContent() {
        System.out.println("파일 내용:\n" + fileContent);
    }
}

public class ExamFileLoaderMain {
    public static void main(String[] args) {
        FileLoader loader = new FileLoader("sample.txt");
        loader.printFileContent();
    }
}
