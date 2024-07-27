"use server";

import { SigninSchema } from "@/types";
import { redirect, RedirectType } from "next/navigation";

export const signin = async (values: SigninSchema) => {
  if (values.email !== "test@test.com") {
    return { error: "가입되어 있지 않은 메일입니다." };
  } else if (values.password !== "1234qwer") {
    return { error: "올바르지 않은 비밀번호입니다." };
  }
  return { success: "성공적으로 로그인 되었습니다!" };
};
