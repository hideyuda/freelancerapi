import requests


class FreelancerAPI:
    """
    docs:https://developers.freelancer.com/docs/

    実行方法:
      以下のページからaccessTokenを生成
      https://accounts.freelancer.com/settings/develop
      ↓
      python main.py
      ↓
      Enter your auth token: ここにaccessTokenを入力
    """

    def __init__(self, auth_token: str):
        self.auth_token = auth_token
        pass

    def get_projects(
        self,
        query: str = "",
        project_types: list = [],
        min_avg_price: float = 0.0,
        max_avg_price: float = 0.0,
        min_avg_hourly_rate: float = 0.0,
        max_avg_hourly_rate: float = 0.0,
        min_price: float = 0.0,
        max_price: float = 0.0,
        countries: list = [],
        languages: list = [],
        sort_field: str = "time_updated",
    ):
        """
        docs:https://developers.freelancer.com/docs/projects/projects

        query	string (optional) Example: some query
        filterSet of space separated terms used to search project names and descriptions.

        project_types[]	array[enum[string]] (optional)
        filterReturns projects with the specific type.

        max_avg_price	decimal (optional) Example: 2.0
        filterReturns projects with the specified maximum average bid in USD.

        min_avg_hourly_rate	decimal (optional) Example: 1.0
        filterReturns projects with the specified minimum hourly bid rate in USD.

        max_avg_hourly_rate	decimal (optional) Example: 1.0
        filterReturns projects with the specified maximum hourly bid rate in USD.

        min_price	decimal (optional) Example: 1.0
        filterReturns projects with a minimum fixed price budget that’s greater than or equal to the specified value in USD.

        max_price	decimal (optional) Example: 10.0
        filterReturns projects with a maximum fixed price budget that’s less than or equal to the specified value in USD.

        min_hourly_rate	decimal (optional) Example: 5.0
        filterReturns projects with a minimum hourly rate budget that’s greater than or equal to the specified value in USD.

        max_hourly_rate	decimal (optional) Example: 15.0
        filterReturns projects with a maximum hourly rate budget that’s less than or equal to the specified value in USD.

        jobs[]	array[number] (optional) Example: 1, 2
        filterReturns projects with at least one of the specified job IDs.

        countries[]	array[string] (optional) Example: au, us
        filterReturns projects with at least one of the specified country codes.

        languages[]	array[string] (optional) Example: en, es
        filterReturns projects with at least one of the specified language IDs.
        """
        query_param = f"query={query}&"
        project_types_param = ""
        for project_type in project_types:
            project_types_param += f"project_types[]={project_type}&"
        min_avg_price_param = f"min_avg_price={min_avg_price}&"
        max_avg_price_param = f"max_avg_price={max_avg_price}&"
        min_avg_hourly_rate_param = f"min_avg_hourly_rate={min_avg_hourly_rate}&"
        max_avg_hourly_rate_param = f"max_avg_hourly_rate={max_avg_hourly_rate}&"
        min_price_param = f"min_price={min_price}&"
        max_price_param = f"max_price={max_price}&"
        countries_param = ""
        for country in countries:
            countries_param += f"countries[]={country}&"
        languages_param = ""
        for language in languages:
            languages_param += f"languages[]={language}&"

        sort_field_param = f"sort_field={sort_field}&"

        params = f"{query_param}{project_types_param}{min_avg_price_param}{max_avg_price_param}{min_avg_hourly_rate_param}{max_avg_hourly_rate_param}{min_price_param}{max_price_param}{countries_param}{languages_param}{sort_field_param}"

        url = f"https://www.freelancer.com/api/projects/0.1//projects/active/?{params}"

        headers = {"freelancer-oauth-v1": self.auth_token}

        print(url)

        response = requests.get(url, headers=headers)

        res_json: dict = response.json()

        result = res_json.get("result")

        return result

    def get_jobs(
        self,
        jobs: list = [],
        job_names: list = [],
        seo_urls: list = [],
        seo_texts: list = [],
        categories: list = [],
        only_local: bool = False,
        seo_details: bool = True,
        seo_country_name: str = "en",
        lang: str = "en",
    ):
        """
        docs:https://developers.freelancer.com/docs/projects/jobs

        Parameter:
        jobs[]	array[number] (optional) Example: 1, 2
        filterReturns jobs with the specified job IDs.

        job_names[]	array[string] (optional) Example: PHP
        filterReturns jobs where the specified strings are sub-strings of the job’s name.

        seo_urls[]	array[string] (optional) Example: content-writing
        filterReturns jobs where the specified strings are sub-strings of the job’s SEO URL.

        seo_texts[]	array[string] (optional) Example: PHP Developer
        filterReturns jobs where the specified strings are sub-strings of the job’s SEO text.

        categories[]	array[number] (optional)
        filterReturns jobs within a specific category.

        only_local	boolean (optional)
        filterReturns only local jobs

        seo_details	boolean (optional)
        projectionReturns SEO information about the returned jobs.

        seo_country_name	string (optional) Example: Australia
        projectionPopulates SEO text with information specific to this country.

        lang	string (optional) Example: en
        projectionLanguage code of the returned values.
        """
        jobs_params = ""
        for job in jobs:
            jobs_params += f"jobs[]={job}&"
        job_names_params = ""
        for job_name in job_names:
            job_names_params += f"job_names[]={job_name}&"
        seo_urls_params = ""
        for seo_url in seo_urls:
            seo_urls_params += f"seo_urls[]={seo_url}&"
        seo_texts_params = ""
        for seo_text in seo_texts:
            seo_texts_params += f"seo_texts[]={seo_text}&"
        categories_params = ""
        for category in categories:
            categories_params += f"categories[]={category}&"
        only_local_param = f"only_local={only_local}&"
        seo_details_param = f"seo_details={seo_details}&"
        seo_country_name_param = f"seo_country_name={seo_country_name}&"
        lang = "en"
        lang_param = f"lang={lang}&"

        params = f"{jobs_params}{job_names_params}{seo_urls_params}{seo_texts_params}{categories_params}{seo_details_param}{seo_country_name_param}{lang_param}"

        url = f"https://www.freelancer.com/api/projects/0.1/jobs/search/?{params}"

        headers = {"freelancer-oauth-v1": self.auth_token}

        print(url)

        response = requests.get(url, headers=headers)

        res_json: dict = response.json()
        # print(res_json)

        result = res_json.get("result")

        return result


if __name__ == "__main__":
    auth_token = input("Enter your auth token: ")
    freelancer = FreelancerAPI(auth_token)
    # result = freelancer.get_jobs(
    #     job_names=["Python", "Django"],
    #     categories=[1],
    #     # seo_texts=["Python", "Django"],
    #     lang="en",
    # )
    # print(result)

    result = freelancer.get_projects(
        query="PHP",
        sort_field="time_updated",
    )
    print(result)
