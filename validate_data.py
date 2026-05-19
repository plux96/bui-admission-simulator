"""
BUI QABUL SIMULYATORI — MA'LUMOTLAR TO'LIQLIGI TEKSHIRUVI (v2)
25 bo'lim, 1000+ parametr
"""

from data_schema import BARCHA_BOLIMLAR, YONALISHLAR, RAQOBATCHILAR


def count_params(data, path=""):
    """Rekursiv: jami, to'ldirilgan, bo'sh maydonlar."""
    total = 0
    filled = 0
    empty = []

    if isinstance(data, list):
        if len(data) == 0:
            return 1, 0, [path or "list"]
        # Ro'yxatdagi birinchi elementni tekshir
        if len(data) > 0 and isinstance(data[0], dict):
            t, f, e = count_params(data[0], path + "[0]")
            return t, f, e
        return 1, (1 if len(data) > 0 else 0), ([] if len(data) > 0 else [path])

    if isinstance(data, dict):
        for key, val in data.items():
            cp = f"{path}.{key}" if path else key
            if isinstance(val, dict):
                t, f, e = count_params(val, cp)
                total += t; filled += f; empty.extend(e)
            elif isinstance(val, list):
                total += 1
                if len(val) > 0:
                    filled += 1
                    # Agar list ichida dict bo'lsa, ularni ham sana
                    if isinstance(val[0], dict):
                        t, f, e = count_params(val[0], cp + "[0]")
                        total += t; filled += f; empty.extend(e)
                else:
                    empty.append(cp)
            elif isinstance(val, bool):
                total += 1; filled += 1
            elif isinstance(val, (int, float)):
                total += 1
                if val != 0:
                    filled += 1
                else:
                    empty.append(cp)
            elif isinstance(val, str):
                total += 1
                if val.strip():
                    filled += 1
                else:
                    empty.append(cp)
            else:
                total += 1
        return total, filled, empty

    return 0, 0, []


def validate():
    grand_total = 0
    grand_filled = 0

    print("=" * 75)
    print("  BUI QABUL SIMULYATORI — MA'LUMOTLAR TO'LIQLIGI (v2)")
    print("  25 bo'lim | 1000+ parametr")
    print("=" * 75)

    results = []
    for name, data in BARCHA_BOLIMLAR.items():
        total, filled, empty = count_params(data)
        grand_total += total
        grand_filled += filled
        pct = (filled / total * 100) if total > 0 else 0

        if pct == 100:
            status = "  OK  "
            icon = "[+]"
        elif pct >= 50:
            status = "QISMAN"
            icon = "[~]"
        else:
            status = " KERAK"
            icon = "[-]"

        results.append((name, total, filled, pct, status, icon, empty))

    # Chiroyli jadval
    for name, total, filled, pct, status, icon, empty in results:
        bar_len = 20
        filled_bar = int(pct / 100 * bar_len)
        bar = "#" * filled_bar + "." * (bar_len - filled_bar)

        print(f"\n  {icon} {name}")
        print(f"      [{bar}] {filled}/{total} ({pct:.0f}%)")

        if pct < 100 and empty:
            shown = empty[:3]
            for field in shown:
                print(f"        - {field}")
            if len(empty) > 3:
                print(f"        ... va yana {len(empty) - 3} ta")

    # Umumiy natija
    pct = (grand_filled / grand_total * 100) if grand_total > 0 else 0

    print(f"\n{'=' * 75}")
    print(f"  JAMI PARAMETRLAR: {grand_total}")
    print(f"  TO'LDIRILGAN:     {grand_filled} ({pct:.0f}%)")
    print(f"  BO'SH:            {grand_total - grand_filled}")
    print(f"{'=' * 75}")

    # Progress bar
    bar_len = 50
    filled_bar = int(pct / 100 * bar_len)
    bar = "#" * filled_bar + "." * (bar_len - filled_bar)
    print(f"\n  [{bar}] {pct:.1f}%")

    if pct < 30:
        print("\n  STATUS: Ma'lumotlar juda kam. Asosiy bo'limlardan boshlang!")
        print("  TAVSIYA: Avval 1, 2, 3, 5, 6 bo'limlarni to'ldiring.")
    elif pct < 50:
        print("\n  STATUS: Boshlang'ich ma'lumotlar bor. Davom eting!")
    elif pct < 70:
        print("\n  STATUS: Yaxshi! Asosiy ma'lumotlar bor.")
    elif pct < 90:
        print("\n  STATUS: Juda yaxshi! Simulyatsiyani boshlash mumkin.")
    else:
        print("\n  STATUS: MUKAMMAL! To'liq simulyatsiyaga tayyor!")

    # Maxsus tekshiruvlar
    print(f"\n{'=' * 75}")
    print("  MAXSUS TEKSHIRUVLAR")
    print(f"{'=' * 75}")

    warnings = []
    if len(YONALISHLAR) < 5:
        warnings.append(f"Yo'nalishlar: {len(YONALISHLAR)} ta (kamida 5-10 kerak)")
    if len(RAQOBATCHILAR) < 3:
        warnings.append(f"Raqobatchilar: {len(RAQOBATCHILAR)} ta (kamida 5-8 kerak)")

    from data_schema import ABITURIYENT_PROFILI
    h = ABITURIYENT_PROFILI.get("hududiy_taqsimot", {})
    jami = sum(v for v in h.values() if isinstance(v, (int, float)))
    if jami > 0 and abs(jami - 100) > 1:
        warnings.append(f"Hududiy taqsimot = {jami}% (100% bo'lishi kerak!)")

    from data_schema import SIMULYATSIYA_MAQSADLAR
    maqsadlar = [SIMULYATSIYA_MAQSADLAR.get(f"maqsad_{i}", {}).get("og_irligi", 0) for i in range(1, 8)]
    jami_maqsad = sum(maqsadlar)
    if jami_maqsad > 0 and abs(jami_maqsad - 1.0) > 0.01:
        warnings.append(f"Maqsad og'irliklari = {jami_maqsad:.2f} (1.00 bo'lishi kerak!)")

    if warnings:
        for w in warnings:
            print(f"  ! {w}")
    else:
        print("  Barcha tekshiruvlar o'tdi!")

    # Prioritet bo'limlar
    print(f"\n{'=' * 75}")
    print("  TO'LDIRISH TARTIBI (PRIORITET)")
    print(f"{'=' * 75}")
    sorted_results = sorted(results, key=lambda x: x[3])  # % bo'yicha saralash
    for i, (name, total, filled, pct, _, _, _) in enumerate(sorted_results[:10], 1):
        print(f"  {i:2d}. {name:<35s} {filled:>3d}/{total:<3d} ({pct:.0f}%)")


if __name__ == "__main__":
    validate()
