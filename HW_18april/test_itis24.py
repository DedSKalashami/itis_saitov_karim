import pytest
import pandas as pd

from itis24 import AdvancedStudentAnalytics


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "name": [
            "Bryan Fitzgerald",
            "Jessica Lawson",
            "Vicki Martin",
            "Heidi Mcmillan",
            "Cynthia Gray"
        ],
        "group": ["B2", "C1", "B1", "C1", "C1"],
        "math": [77, 56, 58, 57, 61],
        "physics": [98, 66, 98, 51, 51],
        "cs": [51, 84, 65, 90, 85],
        "attendance": [82, 55, 70, 58, 91],
        "city": [
            "Saint Petersburg",
            "Novosibirsk",
            "Moscow",
            "Saint Petersburg",
            "Kazan"
        ],
        "enrollment_year": [2022, 2021, 2023, 2020, 2022],
        "scholarship": [True, False, False, True, False],
        "project_score": [88, None, 75, 92, None]
    })


@pytest.fixture
def analytics(sample_df):
    return AdvancedStudentAnalytics(sample_df)


def test_prepare_data_fills_project_score_median(analytics):
    assert analytics.df["project_score"].isna().sum() == 0


def test_prepare_data_creates_average_grade(analytics, sample_df):
    assert "average_grade" in analytics.df.columns

    first_name = sample_df.iloc[0]["name"]
    expected_avg = sample_df.iloc[0][["math", "physics", "cs"]].mean()

    actual_avg = analytics.df.loc[
        analytics.df["name"] == first_name, "average_grade"
    ].iloc[0]

    assert actual_avg == expected_avg


def test_prepare_data_creates_performance_level(analytics):
    assert "performance_level" in analytics.df.columns

    expected_levels = {
        "Bryan Fitzgerald": "medium",
        "Jessica Lawson": "low",
        "Vicki Martin": "medium",
        "Heidi Mcmillan": "low",
        "Cynthia Gray": "low",
    }

    for student_name, expected_level in expected_levels.items():
        actual_level = analytics.df.loc[
            analytics.df["name"] == student_name, "performance_level"
        ].iloc[0]
        assert actual_level == expected_level


def test_prepare_data_creates_risk_level(analytics):
    assert "risk_level" in analytics.df.columns

    expected_risks = {
        "Bryan Fitzgerald": "low risk",
        "Jessica Lawson": "high risk",
        "Vicki Martin": "medium risk",
        "Heidi Mcmillan": "high risk",
        "Cynthia Gray": "low risk",
    }

    for student_name, expected_risk in expected_risks.items():
        actual_risk = analytics.df.loc[
            analytics.df["name"] == student_name, "risk_level"
        ].iloc[0]
        assert actual_risk == expected_risk


def test_top_students_returns_top_n(analytics, sample_df):
    top_students = analytics.top_students(2)

    expected_order = (
        sample_df.assign(
            expected_average=sample_df[["math", "physics", "cs"]].mean(axis=1)
        )
        .sort_values(by="expected_average", ascending=False)["name"]
        .head(2)
        .tolist()
    )

    actual_order = top_students["name"].tolist()

    assert len(top_students) == 2
    assert actual_order == expected_order


def test_group_stats_returns_group_statistics(analytics, sample_df):
    stats = analytics.group_stats()

    assert "average_grade" in stats.columns
    assert "attendance" in stats.columns
    assert "count" in stats.columns

    expected_counts = sample_df.groupby("group")["name"].count()

    for group_name, expected_count in expected_counts.items():
        assert stats.loc[group_name, "count"] == expected_count


def test_at_risk_students_returns_only_high_risk(analytics):
    at_risk = analytics.at_risk_students()

    assert all(at_risk["risk_level"] == "high risk")

    expected_names = {
        "Jessica Lawson",
        "Heidi Mcmillan",
    }

    assert set(at_risk["name"]) == expected_names

def test_scholarship_analysis_returns_mean_values(analytics):
    result = analytics.scholarship_analysis()

    assert "average_grade" in result.columns
    assert "attendance" in result.columns
    assert True in result.index
    assert False in result.index


def test_city_performance_returns_best_and_worst_city(analytics, sample_df):
    city_avg = (
        sample_df.assign(
            expected_average=sample_df[["math", "physics", "cs"]].mean(axis=1)
        )
        .groupby("city")["expected_average"]
        .mean()
    )

    expected_best = city_avg.idxmax()
    expected_worst = city_avg.idxmin()

    result = analytics.city_performance()

    assert isinstance(result, dict)
    assert result["best"] == expected_best
    assert result["worst"] == expected_worst


def test_hidden_top_students(analytics, sample_df):
    expected = sample_df.assign(
        expected_average=sample_df[["math", "physics", "cs"]].mean(axis=1)
    )
    expected = expected[
        (expected["expected_average"] > 85) & (expected["scholarship"] == False)
    ]

    actual = analytics.hidden_top_students()

    assert set(actual["name"]) == set(expected["name"])


def test_lazy_geniuses(analytics, sample_df):
    expected = sample_df.assign(
        expected_average=sample_df[["math", "physics", "cs"]].mean(axis=1)
    )
    expected = expected[
        (expected["expected_average"] > 85) & (expected["attendance"] < 60)
    ]

    actual = analytics.lazy_geniuses()

    assert set(actual["name"]) == set(expected["name"])


def test_performance_distribution(analytics):
    distribution = analytics.performance_distribution()

    assert isinstance(distribution, dict)
    assert round(sum(distribution.values()), 5) == 100.0
    assert "high" in distribution or "medium" in distribution or "low" in distribution


def test_recommendations_returns_list(analytics):
    recommendations = analytics.recommendations()

    assert isinstance(recommendations, list)
    assert len(recommendations) > 0


def test_full_analysis_returns_dict(analytics):
    result = analytics.full_analysis()

    assert isinstance(result, dict)
    assert "top_3" in result
    assert "groups" in result
    assert "at_risk_count" in result
    assert "hidden_tops" in result
    assert "lazy_count" in result
    assert "cities" in result
    assert "scholarship_stats" in result
    assert "performance_distribution" in result
    assert "recommendations" in result


def test_validate_columns_raises_error_when_missing_column():
    bad_df = pd.DataFrame({
        "name": ["Bryan Fitzgerald"],
        "group": ["B2"],
        "math": [77],
        "physics": [98],
        "cs": [51],
        "attendance": [82],
        "city": ["Saint Petersburg"],
        "enrollment_year": [2022],
        "scholarship": [True]
    })

    with pytest.raises(ValueError):
        AdvancedStudentAnalytics(bad_df)