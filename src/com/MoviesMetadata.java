import org.json.JSONArray;
import org.json.JSONObject;

public class MoviesMetadata {
	boolean adult;
	JSONObject belongs_to_collection;
	long budget;
	JSONArray genres;
	String homepage;
	long id;
	String imdb_id;
	String original_language;
	String original_title;
	String overview;
	float popularity;
	String poster_path;
	JSONArray production_companies;
	JSONArray production_countries;
	String release_date;
	long revenue;
	Integer runtime;
	JSONArray spoken_languages;
	String status;
	String tagline;
	String title;

	public boolean isAdult() {
		return adult;
	}

	public void setAdult(boolean adult) {
		this.adult = adult;
	}

	public JSONObject getBelongs_to_collection() {
		return belongs_to_collection;
	}

	public void setBelongs_to_collection(JSONObject belongs_to_collection) {
		this.belongs_to_collection = belongs_to_collection;
	}

	public long getBudget() {
		return budget;
	}

	public void setBudget(long budget) {
		this.budget = budget;
	}

	public JSONArray getGenres() {
		return genres;
	}

	public void setGenres(JSONArray genres) {
		this.genres = genres;
	}

	public String getHomepage() {
		return homepage;
	}

	public void setHomepage(String homepage) {
		this.homepage = homepage;
	}

	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public String getImdb_id() {
		return imdb_id;
	}

	public void setImdb_id(String imdb_id) {
		this.imdb_id = imdb_id;
	}

	public String getOriginal_language() {
		return original_language;
	}

	public void setOriginal_language(String original_language) {
		this.original_language = original_language;
	}

	public String getOriginal_title() {
		return original_title;
	}

	public void setOriginal_title(String original_title) {
		this.original_title = original_title;
	}

	public String getOverview() {
		return overview;
	}

	public void setOverview(String overview) {
		this.overview = overview;
	}

	public float getPopularity() {
		return popularity;
	}

	public void setPopularity(float popularity) {
		this.popularity = popularity;
	}

	public String getPoster_path() {
		return poster_path;
	}

	public void setPoster_path(String poster_path) {
		this.poster_path = poster_path;
	}

	public JSONArray getProduction_companies() {
		return production_companies;
	}

	public void setProduction_companies(JSONArray production_companies) {
		this.production_companies = production_companies;
	}

	public JSONArray getProduction_countries() {
		return production_countries;
	}

	public void setProduction_countries(JSONArray production_countries) {
		this.production_countries = production_countries;
	}

	public String getRelease_date() {
		return release_date;
	}

	public void setRelease_date(String release_date) {
		this.release_date = release_date;
	}

	public long getRevenue() {
		return revenue;
	}

	public void setRevenue(long revenue) {
		this.revenue = revenue;
	}

	public Integer getRuntime() {
		return runtime;
	}

	public void setRuntime(Integer runtime) {
		this.runtime = runtime;
	}

	public JSONArray getSpoken_languages() {
		return spoken_languages;
	}

	public void setSpoken_languages(JSONArray spoken_languages) {
		this.spoken_languages = spoken_languages;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public String getTagline() {
		return tagline;
	}

	public void setTagline(String tagline) {
		this.tagline = tagline;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public boolean isVideo() {
		return video;
	}

	public void setVideo(boolean video) {
		this.video = video;
	}

	public float getVote_average() {
		return vote_average;
	}

	public void setVote_average(float vote_average) {
		this.vote_average = vote_average;
	}

	public int getVote_count() {
		return vote_count;
	}

	public void setVote_count(int vote_count) {
		this.vote_count = vote_count;
	}

	boolean video;
	float vote_average;
	int vote_count;
}
