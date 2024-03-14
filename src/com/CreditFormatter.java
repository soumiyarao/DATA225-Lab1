import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashSet;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class CreditFormatter {
	public static void main(String args[]) throws Exception {
		String CSV_FILE = "/Users/kripa/Desktop/Kripa/SJSU/225/Lab1/datasets/credits.csv";
		String line = "";
		int j = 0, skipped = 0;
		Set<String> castKeys = new HashSet<>();
		Set<String> creditKeys = new HashSet<>();

		String s = "";

		try (BufferedReader br = new BufferedReader(new FileReader(CSV_FILE))) {
			while (((line = br.readLine()) != null)) {
				Pattern pattern = Pattern.compile("\"(.*?)\",\\s*\"(.*?)\",\\s*(\\d+)");
				Matcher matcher = pattern.matcher(line);


				if (matcher.find()) {
					s = matcher.group(1).replaceAll("\"\"", "\"");
					s = s.replaceAll(", \"\"Tyny\"\"'", "");
					s = s.replaceAll("'character': 'Private detective Kogor.*'", "'character': 'Private detective Kogor'");
					s = s.replaceAll("\\\\x\\w\\w", " ");
					if(s.contains("Imomushi") || s.contains("Erkki Uolevi Lahti")) {
						skipped++;
						continue;
					}
					JSONArray jsonArray1 = new JSONArray(s);

					for (int i = 0; i < jsonArray1.length(); i++) {
						JSONObject jsonObject = jsonArray1.optJSONObject(i);
						// Get the keys of the current JSON object
						System.out.println("Keys in object " + i + ":");
						castKeys.addAll(jsonObject.keySet());
					}
					String s2 = matcher.group(2);

					s2 = s2.replaceAll("\"\"", "\"");
					System.out.println(s2);
					JSONArray jsonArray2 = new JSONArray(s2);

					for (int i = 0; i < jsonArray2.length(); i++) {
						JSONObject jsonObject = jsonArray2.optJSONObject(i);
						creditKeys.addAll(jsonObject.keySet());
					}
					int id = Integer.parseInt(matcher.group(3));

					j++;
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		System.out.println(castKeys);
		System.out.println(creditKeys);
		System.out.println(skipped);
	}
}

