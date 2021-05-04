
public class PrefixAndSuffixSearch {

    private String[] words;

    public PrefixAndSuffixSearch(String[] words){
        this.words = words;
    }


	public int solution(String prefix, String suffix){

        System.out.println(words.length-1);

        for(int i = words.length-1; i>=0;i--){
            System.out.println(words[i]);
            System.out.println(words[i].startsWith(prefix));
            System.out.println(words[i].endsWith(suffix));
            if(words[i].startsWith(prefix) && words[i].endsWith(suffix)) return i;
        }

        return -1;
    }
}


