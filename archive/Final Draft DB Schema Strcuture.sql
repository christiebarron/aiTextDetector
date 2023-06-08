-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/J6gSUY
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "essay_raw" (
    "essay_id_sql" int   NOT NULL,
    "essay" text   NOT NULL,
    CONSTRAINT "pk_essay_raw" PRIMARY KEY (
        "essay_id_sql"
     )
);

CREATE TABLE "essay_metadata" (
    "essay_id_sql" int   NOT NULL,
    "essay_set" int   NOT NULL,
    "ai_llm" varchar   NOT NULL,
    "ai_generated" int   NOT NULL,
    CONSTRAINT "pk_essay_metadata" PRIMARY KEY (
        "essay_id_sql"
     )
);

CREATE TABLE "essay_tokens" (
    "essay_id_sql" int   NOT NULL,
    "word_tokens" text   NOT NULL,
    "sentence_tokens" text   NOT NULL,
    "lemmatized_word_tokens" text   NOT NULL,
    CONSTRAINT "pk_essay_tokens" PRIMARY KEY (
        "essay_id_sql"
     )
);

CREATE TABLE "essay_features_continuous" (
    "essay_id_sql" int   NOT NULL,
    "rare_word_count" int   NOT NULL,
    "avg_sentence_length" int   NOT NULL,
    "avg_parse_tree_depth" int   NOT NULL,
    "parse_tree_depth_variation" int   NOT NULL,
    "avg_adjectives_per_sentence" int   NOT NULL,
    "avg_adverbs_per_sentence" int   NOT NULL,
    "avg_verbs_per_sentence" int   NOT NULL,
    "avg_nouns_per_sentence" int   NOT NULL,
    "flesch_reading_ease" int   NOT NULL,
    "flesch_kincaid_grade_level" int   NOT NULL,
    "smog_index" int   NOT NULL,
    "sentiment_polarity" int   NOT NULL,
    "sentiment_subjectivity" int   NOT NULL,
    "perplexity" int   NOT NULL,
    "total_word_count" int   NOT NULL,
    "avg_word_length" int   NOT NULL,
    "TTR" int   NOT NULL,
    "stop_word_count" int   NOT NULL,
    "unique_word_count" int   NOT NULL,
    CONSTRAINT "pk_essay_features_continuous" PRIMARY KEY (
        "essay_id_sql"
     )
);

CREATE TABLE "essay_features_string" (
    "essay_id_sql" int   NOT NULL,
    "word_freq" text   NOT NULL,
    "bigram_freq" text   NOT NULL,
    "trigram_freq" text   NOT NULL,
    CONSTRAINT "pk_essay_features_string" PRIMARY KEY (
        "essay_id_sql"
     )
);

CREATE TABLE "student_id" (
    "student_id" varchar   NOT NULL,
    "student_name" varchar   NOT NULL,
    CONSTRAINT "pk_student_id" PRIMARY KEY (
        "student_id"
     )
);

CREATE TABLE "student_metadata" (
    "student_id" varchar   NOT NULL,
    "student_pseudonym" varchar   NOT NULL,
    "student_grade" int   NOT NULL,
    CONSTRAINT "pk_student_metadata" PRIMARY KEY (
        "student_id"
     )
);

CREATE TABLE "teacher_id" (
    "teacher_id" varchar   NOT NULL,
    "teacher_name" varchar   NOT NULL,
    CONSTRAINT "pk_teacher_id" PRIMARY KEY (
        "teacher_id"
     )
);

CREATE TABLE "teacher_metadata" (
    "teacher_id" varchar   NOT NULL,
    "teacher_grades" int   NOT NULL,
    CONSTRAINT "pk_teacher_metadata" PRIMARY KEY (
        "teacher_id"
     )
);

CREATE TABLE "student_essays" (
    "student_id" varchar   NOT NULL,
    "essay_id_sql" int   NOT NULL,
    CONSTRAINT "pk_student_essays" PRIMARY KEY (
        "student_id","essay_id_sql"
     )
);

-- Free plan table limit reached. SUBSCRIBE for more.



ALTER TABLE "essay_metadata" ADD CONSTRAINT "fk_essay_metadata_essay_id_sql" FOREIGN KEY("essay_id_sql")
REFERENCES "essay_raw" ("essay_id_sql");

ALTER TABLE "essay_tokens" ADD CONSTRAINT "fk_essay_tokens_essay_id_sql" FOREIGN KEY("essay_id_sql")
REFERENCES "essay_raw" ("essay_id_sql");

ALTER TABLE "essay_features_continuous" ADD CONSTRAINT "fk_essay_features_continuous_essay_id_sql" FOREIGN KEY("essay_id_sql")
REFERENCES "essay_raw" ("essay_id_sql");

ALTER TABLE "essay_features_string" ADD CONSTRAINT "fk_essay_features_string_essay_id_sql" FOREIGN KEY("essay_id_sql")
REFERENCES "essay_raw" ("essay_id_sql");

ALTER TABLE "student_metadata" ADD CONSTRAINT "fk_student_metadata_student_id" FOREIGN KEY("student_id")
REFERENCES "student_id" ("student_id");

ALTER TABLE "teacher_metadata" ADD CONSTRAINT "fk_teacher_metadata_teacher_id" FOREIGN KEY("teacher_id")
REFERENCES "teacher_id" ("teacher_id");

ALTER TABLE "student_essays" ADD CONSTRAINT "fk_student_essays_student_id" FOREIGN KEY("student_id")
REFERENCES "student_id" ("student_id");

ALTER TABLE "student_essays" ADD CONSTRAINT "fk_student_essays_essay_id_sql" FOREIGN KEY("essay_id_sql")
REFERENCES "essay_raw" ("essay_id_sql");

-- Free plan table limit reached. SUBSCRIBE for more.



-- Free plan table limit reached. SUBSCRIBE for more.



