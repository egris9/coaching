import {
    weekStart,
    format,
    weekEnd,
    monthStart,
    monthEnd,
} from "https://cdn.jsdelivr.net/npm/@formkit/tempo@0.1.1/+esm";

const sessionOfTheWeekBtn = document.getElementById("sessions_of_the_week_btn");
const sessionOfTheMonthBtn = document.getElementById(
    "sessions_of_the_month_btn"
);

function setFilterPeriodUrlParams(start, end, trigger) {
    const url = new URL(window.location.href);
    url.searchParams.set("filter-by-period-start", start);
    url.searchParams.set("filter-by-period-end", end);
    url.searchParams.set("filter-trigger", trigger);
    return url;
}

function setDateFormat(date) {
    const lang = "en";
    const date_format = "YYYY-MM-DD";
    return format(date, date_format, lang);
}

sessionOfTheWeekBtn.addEventListener("click", () => {
    const current_date = new Date();
    const start_day_index = 1; // sunday is 0

    const start_of_the_week = setDateFormat(
        weekStart(current_date, start_day_index)
    );
    const end_of_the_week = setDateFormat(weekEnd(current_date, start_day_index));

    const url = setFilterPeriodUrlParams(
        start_of_the_week,
        end_of_the_week,
        "week"
    );

    window.location.href = url.href;
});

sessionOfTheMonthBtn.addEventListener("click", () => {
    const current_date = new Date();

    const month_start = setDateFormat(monthStart(current_date));
    const month_end = setDateFormat(monthEnd(current_date));
    const url = setFilterPeriodUrlParams(month_start, month_end, "month");

    window.location.href = url.href;
});