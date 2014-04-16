/*
    Testing syntax highlighting
    of Sublime Text
    for the Linden Scripting Language
*/

integer someIntNormal    = 3672;
integer someIntHex       = 0x00000000;
float   someFloatMath    = PI_BY_TWO;

integer event            = 5673;                                             // unimplemented reserved keyword!

key    someKeyTexture    = TEXTURE_DEFAULT;
string someStringSpecial = EOF;

some_user_defined_function_without_return_type(string inputAsString)
{
    llSay(PUBLIC_CHANNEL, inputAsString);
}

string user_defined_function_returning_a_string(key inputAsKey)
{
    return (string)inputAsKey;
}

default
{
    state_entry()
    {
        key someKey = NULL_KEY;
            someKey = llGetOwner();

        string someString = user_defined_function_returning_a_string(someKey);

        some_user_defined_function_without_return_type(someString);
    }

    touch_start(integer num_detected)
    {
        list    agentsInRegion = llGetAgentList(AGENT_LIST_REGION, []);
        integer numOfAgents    = llGetListLength(agentsInRegion);

        integer index;                                                          // defaults to 0
        for (; index <= numOfAgents - 1; index++)                               // for each agent in region
        {
            llRegionSayTo(llList2Key(agentsInRegion, index), PUBLIC_CHANNEL, "Hello, Avatar!");
        }
    }

    touch_end(integer num_detected)
    {
        someIntNormal       = 3672;
        someIntHex          = 0x00000000;
        someFloatMath       = PI_BY_TWO;

        event               = 5673;                                             // unimplemented reserved keyword!

        someKeyTexture      = TEXTURE_DEFAULT;
        someStringSpecial   = EOF;

        llCloud(ZERO_VECTOR);                                                   // invalid deprecated function!
        llGodLikeRezObject(NULL_KEY, ZERO_VECTOR);                              // god-mode function!

        llWhisper(PUBLIC_CHANNEL, "Leaving \"default\" now...");
        state other;
    }
}

state other
{
    state_entry()
    {
        llWhisper(PUBLIC_CHANNEL, "Entered \"state other\", returning to \"default\" again...");
        state default;
    }
}
