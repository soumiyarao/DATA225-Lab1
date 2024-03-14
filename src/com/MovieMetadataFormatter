import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class MovieMetadataFormatter {
	public static void main(String args[]) throws Exception {
		String TSV_FILE = "/Users/kripa/Downloads/movies_metadata - movies_metadata.tsv";
				// = "/Users/kripa/Desktop/Kripa/SJSU/225/Lab1/datasets/movies_metadata.tsv";
		String line = "";
		int j = 0, skipped = 0;
		Set<String> castKeys = new HashSet<>();
		Set<String> creditKeys = new HashSet<>();

		List<MoviesMetadata> moviesMetadataList = new ArrayList<>();
		//adult	belongs_to_collection	budget	genres	homepage	id	imdb_id	original_language
		// original_title	overview	popularity	poster_path	production_companies	production_countries
		// release_date	revenue	runtime	spoken_languages	status	tagline	title	video	vote_average	vote_count
		String s = "";
		boolean isFirstLine = true;

		try (BufferedReader br = new BufferedReader(new FileReader(TSV_FILE))) {
			while ((line = br.readLine()) != null) {
				if (isFirstLine) {
					isFirstLine = false;
					continue;
				}
				String[] fields = line.split("\t");
				MoviesMetadata m = new MoviesMetadata();
				m.setAdult(Boolean.parseBoolean(fields[0]));

				System.out.println(fields[5]);
				if (fields[1].isEmpty()) {
					m.setBelongs_to_collection(null);
				} else {
					JSONObject jsonObject = new JSONObject(fields[1]);
					m.setBelongs_to_collection(jsonObject);
				}


				m.setBudget(Long.parseLong(fields[2]));

				JSONArray jsonArray = new JSONArray(fields[3]);
				m.setGenres(jsonArray);

				m.setHomepage(fields[4]);
				m.setId(Long.parseLong(fields[5]));
				m.setImdb_id(fields[6]);
				m.setOriginal_language(fields[7]);
				m.setOriginal_title(fields[8]);
				m.setOverview(fields[9]);
				m.setPopularity(Float.parseFloat(fields[10]));
				m.setPoster_path(fields[11]);

				System.out.println(fields[12]);
				try {
					JSONArray prodCompJsonArray = new JSONArray(fields[12]);
					m.setProduction_companies(prodCompJsonArray);
				} catch (JSONException e) {
					s = fields[12].replaceAll("\\\\xa0", "");
					System.out.println(s);
					JSONArray prodCompJsonArray = new JSONArray(s);
					m.setProduction_companies(prodCompJsonArray);
				}
				JSONArray prodCountryJsonArray = new JSONArray(fields[13]);
				m.setProduction_countries(prodCountryJsonArray);
				m.setRelease_date(fields[14]);
				m.setRevenue(Long.parseLong(fields[15]));
				Integer runtime = fields[16].isEmpty() ? null : Integer.parseInt(fields[16]);
				m.setRuntime(runtime);

				try {
					JSONArray splJsonArray = new JSONArray(fields[17]);
					m.setSpoken_languages(splJsonArray);
				} catch (JSONException e) {
					s = fields[12].replaceAll("[^\\x00-\\x7F]", "");
					System.out.println(s);
					JSONArray splJsonArray = new JSONArray(s);
					m.setSpoken_languages(splJsonArray);
				}
				m.setStatus(fields[18]);
				m.setTagline(fields[19]);
				m.setTitle(fields[20]);
				m.setVideo(Boolean.parseBoolean(fields[21]));
				m.setVote_average(Float.parseFloat(fields[22]));
				m.setVote_count(Integer.parseInt(fields[23]));

			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}

