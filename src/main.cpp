namespace REQS
{
struct SystemSaveHook
{
    static void Call(RE::BGSSaveLoadManager* a_manager, uint32_t a_flag)
    {
        static constexpr std::uint32_t button_regular_save = 0xF0000080;
        func(a_manager, button_regular_save);
        return RE::UIMessageQueue::GetSingleton()->AddMessage(RE::JournalMenu::MENU_NAME, RE::UI_MESSAGE_TYPE::kHide,
                                                              nullptr);
    }
    static inline REL::THook func{REL::ID(53274), 0x26, Call};
};

} // namespace REQS

SKSE_PLUGIN_LOAD(const SKSE::LoadInterface* a_skse)
{
    SKSE::Init(a_skse, {.trampoline = true});
    return true;
}
