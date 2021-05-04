package LeetCodeJava.src;

public class PrefixAndSuffixSearch {

    TrieNode trie;

    public PrefixAndSuffixSearch(String[] words){
        trie = new TrieNode();

        for (int weight = 0; weight < words.length; ++weight) {

            String word = words[weight] + "{";

            System.out.println(word);

            for (int i = 0; i < word.length(); ++i) {
                TrieNode cur = trie;
                cur.weight = weight;

                // System.out.println(word.length());
                // System.out.println(2 * word.length() - 1);

                for (int j = i; j < 2 * word.length() - 1; ++j) {
                    
                    int k = word.charAt(j % word.length()) - 'a';
                    System.out.println(cur.children[k]);
                    if (cur.children[k] == null) 
                        cur.children[k] = new TrieNode();
                    cur = cur.children[k];
                    cur.weight = weight;
                }
            }
        }

    }


	public int solution(String prefix, String suffix){

        TrieNode cur = trie;
        
        for (char letter: (suffix + '{' + prefix).toCharArray()) {
            if (cur.children[letter - 'a'] == null) return -1;
            cur = cur.children[letter - 'a'];
        }

        return cur.weight;
    }
}


class TrieNode {
    TrieNode[] children;
    int weight;
    public TrieNode() {
        children = new TrieNode[27];
        weight = 0;
    }
}