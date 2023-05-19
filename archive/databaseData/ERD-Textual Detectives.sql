-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/TBTB9r
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "essay_raw" (
    "essayid_sql" int   NOT NULL,
    "essay" varchar   NOT NULL,
    CONSTRAINT "pk_essay_raw" PRIMARY KEY (
        "essayid_sql"
     )
);

CREATE TABLE "student_id" (
    "student_name" text   NOT NULL,
    "student_id" int   NOT NULL,
    CONSTRAINT "pk_student_id" PRIMARY KEY (
        "student_id"
     )
);

CREATE TABLE "teacher_id" (
    "teacher_name" text   NOT NULL,
    "teacher_id" int   NOT NULL,
    CONSTRAINT "pk_teacher_id" PRIMARY KEY (
        "teacher_id"
     )
);

CREATE TABLE "essay_metadata" (
    "essayid_sql" int   NOT NULL,
    "essay_id" int   NOT NULL,
    "essay_set" int   NOT NULL,
    "ai_llm" text   NOT NULL,
    "ai_generated" int   NOT NULL,
    "student_id" int   NOT NULL
);

CREATE TABLE "essay_tokens" (
    "essayid_sql" int   NOT NULL,
    "word_tokens" varchar   NOT NULL,
    "setence_tokens" varchar   NOT NULL,
    "lemmatized_word_tokens" text   NOT NULL
);

CREATE TABLE "essay_features_continuous" (
    "essayid_sql" int   NOT NULL,
    "total_word_count" numeric   NOT NULL,
    "avg_word_length" numeric   NOT NULL,
    "avg_sentence_length1" numeric   NOT NULL,
    "TTR" numeric   NOT NULL,
    "stop_word_count" numeric   NOT NULL,
    "unique_word_count" numeric   NOT NULL,
    "rare_word_count" numeric   NOT NULL,
    "avg_sentence_length2" numeric   NOT NULL,
    "avg_parse_tree_depth" numeric   NOT NULL,
    "parse_tree_depth_variation" numeric   NOT NULL,
    "avg_adjectives_per_sentence" numeric   NOT NULL,
    "avg_adverbs_per_sentence" numeric   NOT NULL,
    "avg_verbs_per_sentence" numeric   NOT NULL,
    "avg_nouns_per_sentence" numeric   NOT NULL,
    "unknown" numeric   NOT NULL,
    "flesch_reading_ease" numeric   NOT NULL,
    "flesch_kincaid_grade_level" numeric   NOT NULL,
    "sentiment_polarity" numeric   NOT NULL,
    "sentiment_subjectivity" numeric   NOT NULL,
    "perplexity" numeric   NOT NULL
);

CREATE TABLE "essay_features_string" (
    "essayid_sql" int   NOT NULL,
    "word_freq" varchar   NOT NULL,
    "bigram_freq" varchar   NOT NULL,
    "trigram_freq" varchar   NOT NULL
);

CREATE TABLE "teacher_student" (
    "teacher_id" int   NOT NULL,
    -- foreign key
    "student_id" int   NOT NULL
);

CREATE TABLE "student_metadata" (
    "student_id" int   NOT NULL,
    "student_pseudonym" varchar   NOT NULL,
    "student_grade" int   NOT NULL
);

-- student_teachers int FK >-< teacher_id.teacher_id REMOVED AND ADDED DIFF TABLE
-- student_essays int FK -< essay_raw.essayid_sql REMOVED AND ADDED TO ESSAY TABLE
CREATE TABLE "teacher_metadata" (
    -- foreign key
    "teacher_id" int   NOT NULL,
    "teacher_grades" int   NOT NULL
);

ALTER TABLE "essay_metadata" ADD CONSTRAINT "fk_essay_metadata_essayid_sql" FOREIGN KEY("essayid_sql")
REFERENCES "essay_raw" ("essayid_sql");

ALTER TABLE "essay_metadata" ADD CONSTRAINT "fk_essay_metadata_student_id" FOREIGN KEY("student_id")
REFERENCES "student_id" ("student_id");

ALTER TABLE "essay_tokens" ADD CONSTRAINT "fk_essay_tokens_essayid_sql" FOREIGN KEY("essayid_sql")
REFERENCES "essay_raw" ("essayid_sql");

ALTER TABLE "essay_features_continuous" ADD CONSTRAINT "fk_essay_features_continuous_essayid_sql" FOREIGN KEY("essayid_sql")
REFERENCES "essay_raw" ("essayid_sql");

ALTER TABLE "essay_features_string" ADD CONSTRAINT "fk_essay_features_string_essayid_sql" FOREIGN KEY("essayid_sql")
REFERENCES "essay_raw" ("essayid_sql");

ALTER TABLE "teacher_student" ADD CONSTRAINT "fk_teacher_student_teacher_id" FOREIGN KEY("teacher_id")
REFERENCES "teacher_id" ("teacher_id");

ALTER TABLE "teacher_student" ADD CONSTRAINT "fk_teacher_student_student_id" FOREIGN KEY("student_id")
REFERENCES "student_id" ("student_id");

ALTER TABLE "student_metadata" ADD CONSTRAINT "fk_student_metadata_student_id" FOREIGN KEY("student_id")
REFERENCES "student_id" ("student_id");

ALTER TABLE "teacher_metadata" ADD CONSTRAINT "fk_teacher_metadata_teacher_id" FOREIGN KEY("teacher_id")
REFERENCES "teacher_id" ("teacher_id");

